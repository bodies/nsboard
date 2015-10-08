"""
    library.py

    클래스 Library: 소설 관련 DB 작업 처리
"""

import mysql.connector as conn
from config_db import *


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

    def _register_keywords(self, book_num, keywords):
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

    def new_book(self, title, series, public, complete, keywords, intro):
        """
        series, public = 0 / 1
        keywords = 리스트

        TODO:
            1) 새 책 등록하고, 책 번호 받기
            2) 키워드 목록을 루프 돌려서..
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

            self._register_keywords(book_num, keywords)

            return book_num
        except:
            raise

    def modify_book(self, num, title, series, public, complete, keywords, intro):
        """ TODO: keyword_links 테이블에서 사용하지 않는 키워드를
             keywords 테이블에서 삭제하는 "청소" 메서드 만들 것!
        """
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

            self._register_keywords(num, keywords)

        except:
            raise

    def new_story(self, book_num, queue_num, title, story, public):
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

    def modify_story(self, story_num, queue_num, title, story, public):
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

    def story_list(self, book_num, page=1, order='DESC'):
        # TODO: 페이지를 구현할 것!
        try:
            start = (page - 1) * 20
            end = page * 20

            # DESC를 excute()에서 %s로 넘기면, 따옴표가 붙어서 에러 발생함.
            query = 'SELECT num, book_num, queue_num, title, public, view_count,\
                like_count, pub_date, mod_date FROM stories WHERE book_num=%s\
                ORDER BY queue_num {} LIMIT %s, %s'.format(order)
            print('QUERY:', query)

            self.cur.execute(query, (book_num, start, end))

            data = self.cur.fetchall()
            result = []
            for n in data:
                result.append(dict(zip(self.cur.column_names, n)))
            return result
        except Exception as e:
            raise e

    def book_list(self):
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
            print(data)

            data['keywords'] = self.book_keywords(book_num)

            return data

        except Exception as e:
            print(str(e))
            raise
        finally:
            # self.cur.close()
            # self.cnx.close()
            pass

    def story(self, story_num):
        """ TODO:
            * '이전 화 - 다음 화' 링크를 위해 앞뒤 화 존재 여부 확인
            * 원하는 화가 없을 경우, 에러는 어떻게 처리??
        """

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

            self.cur.execute(
                'SELECT story FROM story_data WHERE num=%s LIMIT 1',
                (story_num,))
            result = self.cur.fetchone()

            if not result:
                raise Exception('출력할 내용이 존재하지 않습니다.')

            # data['story'] = result[0].replace('\n', '<br />')
            # 줄바꿈 변화는 사용하는 쪽에서 직접 처리하는 편이 좋은 듯
            data['story'] = result[0]
            data['keywords'] = self.book_keywords(data['book_num'])
            data['story_count'] = self.story_count(data['book_num'])

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

    def story_count(self, book_num):
        try:
            self.cur.execute(
                'SELECT count(*) FROM stories WHERE book_num=%s',
                (book_num,))
            result = self.cur.fetchone()

            if not result:
                return False
            else:
                return result[0]
        except:
            raise

    def queue_dupe_check(self, book_num, queue_num):
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
