"""
    library.py
"""

# TODO 1) DB 커서 해제?

import mysql.connector as conn
from config import *


class Library:

    cnx = None
    cur = None

    def __init__(self):
        try:
            self.cnx = conn.connect(
                user=DB_USER, password=DB_PASSWORD, database=DB_NAME,
                host=DB_HOST, port=DB_PORT, autocommit=True)
            self.cur = self.cnx.cursor()
        except:
            raise

    def __del__(self):
        # TODO: 깔끔한 뒷처리 방법?
        # self.cur.close()
        # self.cnx.close() P
        pass

    # ---- BOOK ---- #

    def book_add(self, title, series, public, complete, keywords, intro):
        """
        :param series: 0/1
        :param public: 0/1
        :param keywords: 리스트

        1) 새 책 등록하고, 책 번호 받기
        2) 키워드 목록을 루프 돌려서
            1. keywords 테이블에서 키워드 찾기
            2. 있으면 키워드 번호 받기 / 없으면 키워드 등록하고 번호 받기
            3. 책 번호 + 키워드 번호가 keyword_links 테이블에 있는지 확인하고 없으면 등
        """
        try:
            # 책 등록 & 책 번호
            self.cur.execute(
                'INSERT INTO books (title, intro, series, public, complete,\
                pub_date, mod_date) VALUES (%s, %s, %s, %s, %s, NOW(), NOW())',
                (title, intro, series, complete, public)
            )
            book_num = self.cur.lastrowid

            # 키워드 등록 & 키워드 번호 & 키워드 링크 등록
            # IGNORE된 것도 lastrowid에 기록되나?

            self.keywords_add(book_num, keywords)
            return book_num
        except:
            raise

    def book_edit(self, num, title, series, public, complete, keywords, intro):
        # TODO: keyword_links 테이블에서 사용하지 않는 키워드를 keywords 테이블에서 삭제하는 "청소" 메서드 만들 것!
        try:
            # ???: UPDATE를 해도 'ON UPDATE CURRENT_TIMESTAMP'가 작동을 안한다.
            # 어쩌면 autocommit과 연관이 있을 지도.. 일단 직접 NOW()로 현재 시각을 넣자
            self.cur.execute(
                'UPDATE books SET title=%s, series=%s, public=%s, complete=%s,\
                intro=%s, mod_date=NOW() WHERE num=%s LIMIT 1',
                (title, series, public, complete, intro, num))

            # keyword_links 갱신: 옛 키워드 제거 & 새 키워드 등록
            old_keywords = self.book_keywords(num)
            for kw in old_keywords:
                self.cur.execute(
                    'DELETE FROM keyword_links WHERE book_num=%s AND\
                    keyword_num=(SELECT num FROM keywords WHERE keyword=%s\
                    LIMIT 1)', (num, kw))
            self.keywords_add(num, keywords)
        except:
            raise

    def book_info(self, book_num):
        try:
            self.cur.execute(
                'SELECT b.num, b.title, b.series, b.public, b.complete,\
                b.intro, b.pub_date, b.mod_date, b.update_date,\
                COUNT(s.num) AS story_count, SUM(view_count) AS view_count,\
                ROUND(AVG(like_count)) AS like_count\
                FROM books AS b, stories AS s\
                WHERE b.num=%s AND b.num=s.book_num LIMIT 1', (book_num,)
            )
            # 'SELECT num, title, series, public, complete, intro, pub_date,\
            # mod_date, update_date, (SELECT COUNT(s.num) FROM stories AS s\
            # WHERE s.book_num=b.num) AS story_count, \
            # (SELECT SUM(s.view_count) FROM stories AS s\
            # WHERE s.book_num=b.num) AS view_count FROM books AS b\
            # WHERE num=%s LIMIT 1', (book_num,))

            result = self.cur.fetchone()

            if not result:
                return False

            data = dict(zip(self.cur.column_names, result))
            data['keywords'] = self.book_keywords(book_num)
            return data
        except Exception as e:
            raise
        finally:
            pass

    # ---- STORY ----#

    def story_add(self, book_num, queue_num, title, story, public):
        try:
            self.cur.execute(
                'INSERT INTO stories (book_num, queue_num, title, public,\
                pub_date, mod_date) VALUES (%s, %s, %s, %s, NOW(), NOW())',
                (book_num, queue_num, title, public))
            story_num = self.cur.lastrowid

            self.cur.execute(
                'INSERT INTO story_data (num, story) VALUES (%s, %s)',
                (story_num, story))

            self.cur.execute(
                'UPDATE books SET update_date=NOW() WHERE num=%s',
                (book_num,))

            return story_num

        except:
            raise

    def story_edit(self, story_num, queue_num, title, story, public):
        try:
            self.cur.execute(
                'UPDATE stories SET queue_num=%s, title=%s, public=%s,\
                mod_date=NOW() WHERE num=%s LIMIT 1',
                (queue_num, title, public, story_num))
            self.cur.execute(
                'UPDATE story_data SET story=%s WHERE num=%s LIMIT 1',
                (story, story_num))
        except:
            raise

    def story_view(self, story_num):
        try:
            self.cur.execute(
                'SELECT num, book_num, queue_num, title, public, view_count,\
                like_count, pub_date, mod_date, (SELECT title FROM books AS b\
                WHERE num=s.book_num LIMIT 1) AS book_title\
                FROM stories AS s WHERE num=%s LIMIT 1', (story_num,))
            result = self.cur.fetchone()

            if not result:
                raise Exception('출력할 내용이 존재하지 않습니다.')

            data = dict(zip(self.cur.column_names, result))

            self.cur.execute('SELECT story FROM story_data WHERE num=%s LIMIT 1', (story_num,))
            result = self.cur.fetchone()

            if not result:
                raise Exception('출력할 내용이 존재하지 않습니다.')

            # data['story'] = result[0].replace('\n', '<br />')
            # 줄바꿈 변화는 사용하는 쪽에서 직접 처리하는 편이 좋은 듯
            data['story'] = result[0]
            data['keywords'] = self.book_keywords(data['book_num'])
            data['story_count'] = self.count_story_by_book(data['book_num'])

            # 이전 화-다음 화 글 번호 지정
            if data['queue_num'] > 1:
                data['prev'] = self.story_num(data['book_num'], data['queue_num'] - 1)
            else:
                data['prev'] = None

            if data['queue_num'] < data['story_count']:
                data['next'] = self.story_num(data['book_num'], data['queue_num'] + 1)
            else:
                data['next'] = None
            return data
        except:
            raise

    # ---- LIST ---- #

    def list_book(self):
        # 책 정보를 사전 형태 반환
        # 번호, 제목, 공개 여부, 완결 여부, 최초 게시일, 최근 게시일, 연재 횟수
        try:
            self.cur.execute(
                'SELECT num, title, public, complete, pub_date, mod_date,\
                update_date,\
                (SELECT count(s.num) from stories AS s WHERE s.book_num=b.num)\
                as story_count FROM books AS b ORDER BY num DESC')
            data = self.cur.fetchall()

            if not data:
                return False

            result = []
            for row in data:
                result.append(dict(zip(self.cur.column_names, row)))
            return result

        except Exception as e:
            print(str(e))
            raise

    def list_book_by_keyword(self, keyword, page=1, per_page=20):
        """ 주어진 키워드에 해당하는 작품 목록을 반환
            작품 번호, 제목, 최종 갱신일, 등록된 글 수

            TODO:
            1. 주어진 키워드의 키워드 번호 확인
            2. 키워드 번호를 가진 작품 번호 조회
            3. 주어진 작품 번호로 작품 정보 목록 반환
        """
        try:
            start = (page - 1) * per_page
            self.cur.execute(
                'SELECT num FROM keywords WHERE keyword=%s LIMIT 1',
                (keyword,))
            result = self.cur.fetchone()
            if not result:
                raise Exception('등록된 키워드가 아닙니다.')
            keyword_num = result[0]

            self.cur.execute(
                'SELECT num, title, update_date,\
                (SELECT count(s.num) FROM stories AS s WHERE s.book_num=b.num)\
                as story_count FROM books AS b\
                WHERE num IN (SELECT book_num FROM keyword_links WHERE keyword_num=%s)\
                ORDER BY update_date DESC LIMIT %s, %s', (keyword_num, start, per_page))
            return self.cur.fetchall()

        except Exception as e:
            raise e

    def list_story_by_book(self, book_num, page=1, per_page=20, order='DESC'):
        """
            주어진 작품(book_num)에 속한 글 목록 반환
        """
        try:
            start = (page - 1) * per_page

            # DESC를 excute()에서 %s로 넘기면, 따옴표가 붙어서 에러 발생함.
            query = 'SELECT num, book_num, queue_num, title, public, view_count,\
                like_count, pub_date, mod_date FROM stories WHERE book_num=%s\
                ORDER BY queue_num {} LIMIT %s, %s'.format(order)
            print('QUERY:', query)

            self.cur.execute(query, (book_num, start, per_page))

            data = self.cur.fetchall()
            result = []
            for n in data:
                result.append(dict(zip(self.cur.column_names, n)))
            return result
        except Exception as e:
            raise e

    def list_story_new(self, page=1, per_page=20):
        # 새로 등록된 작품 목록
        try:
            start = (page - 1) * per_page
            self.cur.execute(
                'SELECT num, title, pub_date, view_count FROM stories\
                ORDER BY pub_date DESC LIMIT %s, %s', (start, per_page))
            # LIMIT 0, 4 => 0부터 시작해서 4개 (0, 1, 2, 3)
            result = self.cur.fetchall()
            return result

        except Exception as e:
            raise e

    def list_story_new_preview(self, page=1, per_page=10):
        # 메인 페이지용 새 글 미리보기 목록
        try:
            start = (page - 1) * per_page
            self.cur.execute(
                'SELECT num, title, pub_date,\
                (SELECT LEFT(story, 200) FROM story_data AS d\
                WHERE d.num=s.num) AS preview FROM stories AS s\
                ORDER BY pub_date DESC LIMIT %s, %s', (start, per_page))
            result = self.cur.fetchall()
            return result
        except Exception as e:
            raise e

    def list_hot(self, page=1, per_page=20):
        # 조회수가 가장 많은 글 목록
        # TODO: 용도에 맞게 메서드 이름 고칠 것!
        try:
            start = (page - 1) * per_page
            self.cur.execute(
                'SELECT num, title, pub_date FROM stories\
                ORDER BY pub_date DESC LIMIT %s, %s', (start, per_page))
            # LIMIT 0, 4 => 0부터 시작해서 4개 (0, 1, 2, 3)
            result = self.cur.fetchall()
            return result

        except Exception as e:
            raise e

    def list_keywords(self):
        # 키워드 전체 목록을 반환
        # TODO: 다양한 키워드 목록을 보여줄까? (인기순 등)
        try:
            self.cur.execute(
                'SELECT keyword FROM keywords ORDER BY keyword ASC')
            result = self.cur.fetchall()
            return result
        except Exception as e:
            raise e

    def story_num(self, book_num, queue_num):
        # 작품 내 연재 번호로 글 번호 찾아서 반환
        try:
            self.cur.execute(
                'SELECT num FROM stories WHERE book_num=%s AND queue_num=%s LIMIT 1',
                (book_num, queue_num))
            result = self.cur.fetchone()
            if not result:
                raise Exception('출력할 내용이 존재하지 않습니다.')
            else:
                return result[0]
        except:
            raise

    def book_num(self, story_num):
        try:
            self.cur.execute(
                'SELECT book_num FROM stories WHERE num=%s LIMIT 1',
                (story_num,))
            result = self.cur.fetchone()
            if not result:
                return False
            else:
                return result[0]
        except:
            raise

    def book_name(self, book_num):
        try:
            self.cur.execute(
                'SELECT title FROM books WHERE num=%s LIMIT 1',
                (book_num,))
            result = self.cur.fetchone()

            if not result:
                return False
            else:
                return result[0]
        except:
            raise

    def book_keywords(self, book_num):
        try:
            self.cur.execute(
                'SELECT keyword FROM keywords WHERE num IN (SELECT keyword_num\
                FROM keyword_links WHERE book_num=%s)', (book_num,))
            result = self.cur.fetchall()

            if result:
                # 튜플 리스트인 결과값을 그냥 리스트로 변환
                result = [i[0] for i in result]
            return result

        except Exception as e:
            print(str(e))
            raise

    # ---- COUNT ---- #

    def count_story_by_book(self, book_num):
        try:
            self.cur.execute('SELECT count(*) FROM stories WHERE book_num=%s', (book_num,))
            result = self.cur.fetchone()

            if not result:
                return False
            else:
                return result[0]
        except:
            raise

    def count_story_all(self):
        # 모든 글 갯수
        try:
            self.cur.execute('SELECT count(*) FROM stories')
            result = self.cur.fetchone()
            return result[0]
        except:
            raise

    def count_book_by_keyword(self, keyword):
        # 키워드에 해당하는 작품의 갯수를 반환
        # TODO: 쿼리를 하나로 합칠 것!
        try:
            self.cur.execute(
                'SELECT num FROM keywords WHERE keyword=%s LIMIT 1',
                (keyword,))
            result = self.cur.fetchone()
            keyword_num = result[0]

            self.cur.execute(
                'SELECT COUNT(DISTINCT(book_num)) FROM keyword_links WHERE keyword_num=%s',
                (keyword_num,))
            result = self.cur.fetchone()
            return result[0]
        except Exception as e:
            raise e

    # ---- KEYWORDS ---- #

    def keywords_add(self, book_num, keywords):
        try:
            for kw in keywords:
                self.cur.execute(
                    'INSERT IGNORE INTO keywords (keyword) VALUES (%s)', (kw, ))
                self.cur.execute(
                    'SELECT num from keywords WHERE keyword=%s', (kw, ))
                result = self.cur.fetchone()
                kw_num = result[0]

                self.cur.execute(
                    'SELECT EXISTS (SELECT 1 FROM keyword_links\
                    WHERE book_num=%s AND keyword_num=%s LIMIT 1)',
                    (book_num, kw_num))
                result = self.cur.fetchone()
                if not result[0]:
                    self.cur.execute(
                        'INSERT INTO keyword_links (book_num, keyword_num)\
                        VALUES (%s, %s)', (book_num, kw_num))
        except:
            raise

    def keywords_clean(self):
        # 키워드 테이블을 검색해서 빈 키워드면 삭제
        try:
            self.cur.execute(
                'SELECT num, keyword FROM keywords')
            keywords = self.cur.fetchall()
            for row in keywords:
                if row[1].strip() == '':
                    self.cur.execute(
                        'DELETE FROM keywords WHERE num=%s', (row[0],))
                    self.cur.execute(
                        'DELETE FROM keyword_links WHERE keyword_num=%s', (row[0],))
            return True
        except Exception as e:
            raise e

    # ---- LIKE ---- #

    def like_dupe_check(self, story_num, ip):
        try:
            self.cur.execute(
                'SELECT count(*) FROM likes WHERE story_num=%s AND ip=INET_ATON(%s)', (story_num, ip)
            )
            result = self.cur.fetchone()

            if result[0]:
                return True
            else:
                return False
        except Exception as e:
            print("DUPE CHECK ERROR!")
            raise e

    def like_add(self, story_num, ip):
        """
            1. 테이블 likes에 글번호-IP 등록
            2. 테이블 stories에 추천 + 1
            3. (미구현) 테이블 books에 추천 + 1
        """
        # TODO: books 테이블도 추천수 + 1
        try:
            self.cur.execute(
                'INSERT INTO likes (story_num, ip) VALUES (%s, INET_ATON(%s))', (story_num, ip)
            )
            self.cur.execute(
                'UPDATE stories SET like_count=like_count+1 WHERE num=%s', (story_num,)
            )
        except Exception as e:
            raise e

    def like_delete_all(self):
        # LIKES 테이블을 전체 삭제 (주기적으로)
        # TODO: 테이블 전체 삭제 구현
        try:
            pass
        except Exception as e:
            raise e

    # ---- ETC ---- #

    def view_count_add(self, story_num):
        try:
            self.cur.execute(
                'UPDATE stories SET view_count=view_count+1 WHERE num=%s',
                (story_num,))
        except Exception as e:
            raise e

    def check_dupe_queue(self, book_num, queue_num):
        try:
            self.cur.execute(
                'SELECT EXISTS (SELECT 1 FROM stories WHERE book_num=%s AND\
                queue_num=%s LIMIT 1)', (book_num, queue_num))

            result = self.cur.fetchone()
            print('QUEUE_DUPE_CHECK:', result)
            if result[0]:
                return True
            else:
                return False
        except:
            raise

    def match_queue_num(self, story_num, queue_num):
        try:
            self.cur.execute(
                'SELECT count(*) FROM stories WHERE num=%s AND queue_num=%s',
                (story_num, queue_num))
            result = self.cur.fetchone()
            return result[0]
        except:
            raise