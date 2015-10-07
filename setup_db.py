"""
    setup_db.py

    TODO:
        1) 백업 스크립트 만들 것
"""

import mysql.connector as conn
from mysql.connector import errorcode
from config_db import *

TABLES = []

# 책
# stories의 부모 역할
# users(num)을 외부키로 사용하고, book이 존재하면 user 삭제는 제한(RESTRICT)
q = (
    "CREATE TABLE books ("
    " num mediumint UNSIGNED AUTO_INCREMENT,"
    " title varchar(255) NOT NULL,"
    " intro text,"
    " series tinyint(1) NOT NULL DEFAUL 1,"
    " public tinyint(1) NOT NULL DEFAULT 0,"
    " complete tinyint(1) NOT NULL DEFAULT 0,"
    " pub_date datetime NOT NULL DEFAULT 0,"
    " mod_date datetime NOT NULL DEFAULT 0 ON UPDATE CURRENT_TIMESTAMP,"
    " update_date datetime NOT NULL DEFAULT 0,"
    " PRIMARY KEY(num)"
    ")"
)
TABLES.append(('books', q))

# 글
# 글에 대한 메타 데이터 저장
# story_data의 부모
q = (
    "CREATE TABLE stories ("
    " num mediumint UNSIGNED AUTO_INCREMENT,"
    " book_num mediumint UNSIGNED NOT NULL,"
    " queue_num smallint UNSIGNED NOT NULL DEFAULT 0,"
    " title varchar(255) NOT NULL,"
    " public tinyint(1) NOT NULL DEFAULT 0,"
    " view_count mediumint UNSIGNED DEFAULT 0,"
    " like_count mediumint UNSIGNED DEFAULT 0,"
    " pub_date datetime NOT NULL DEFAULT 0,"
    " mod_date datetime NOT NULL DEFAULT 0 ON UPDATE CURRENT_TIMESTAMP,"
    " PRIMARY KEY (num),"
    " FOREIGN KEY (book_num) REFERENCES books(num) ON DELETE RESTRICT"
    ")"
)
TABLES.append(('stories', q))

# 글 내용
# 실제 글의 내용
# num은 stories 테이블을 참조하는 외부 키.
# stories에서 삭제 시, story_data의 해당 항목도 삭제됨.
q = (
    "CREATE TABLE story_data ("
    " num mediumint UNSIGNED NOT NULL,"
    " story mediumtext,"
    " FOREIGN KEY (num) REFERENCES stories(num) ON DELETE CASCADE"
    ")"
)
TABLES.append(('story_data', q))

# 키워드 목록
q = (
    "CREATE TABLE keywords ("
    " num mediumint UNSIGNED AUTO_INCREMENT,"
    " keyword varchar(255) NOT NULL,"
    " PRIMARY KEY (num), UNIQUE (keyword)"
    ")"
)
TABLES.append(('keywords', q))

# 책과 키워드 연결
q = (
    "CREATE TABLE keyword_links ("
    " book_num mediumint UNSIGNED,"
    " keyword_num mediumint UNSIGNED,"
    " FOREIGN KEY (book_num) REFERENCES books(num) ON DELETE CASCADE,"
    " FOREIGN KEY (keyword_num) REFERENCES keywords(num) ON DELETE CASCADE"
    ")"
)
TABLES.append(('keyword_links', q))

# 페이지 방문 여부 확인용
q = (
    "CREATE TABLE views ("
    " story_num mediumint UNSIGNED,"
    " ip int UNSIGNED NOT NULL,"
    " PRIMARY KEY (story_num)"
    ")"
)
TABLES.append(('views', q))

# 추천 여부 확인용
q = (
    "CREATE TABLE likes ("
    " story_num mediumint UNSIGNED,"
    " ip int UNSIGNED NOT NULL,"
    " PRIMARY KEY (story_num)"
    ")"
)
TABLES.append(('likes', q))


# ----- MAIN ----- #

# DB 접속
try:
    cnx = conn.connect(user=DB_USER, password=DB_PASSWORD,
                       host=DB_HOST, port=DB_PORT, autocommit=True)
except conn.Error as e:
    print("DB 접속 실패!: ", e.msg)
    exit()
else:
    cur = cnx.cursor()

# DB 생성


# 테이블 생성
def create_db():
    try:
        print('데이터베이스 {} 생성 중... '.format(DB_NAME), end='')
        global cur
        cur.execute('CREATE DATABASE {}'.format(DB_NAME))
        print('OK!')

    except conn.Error as e:
        if e.errno == errorcode.ER_DB_CREATE_EXISTS:
            print('이미 존재합니다!')
            if ('y' == input('삭제하고 다시 만들까요? (y/n) ').strip().lower()):
                try:
                    print('데이터베이스 {} 삭제 중... '.format(DB_NAME), end='')
                    cur.execute('DROP DATABASE {}'.format(DB_NAME))
                    print('OK!')
                    create_db()
                except:
                    print('삭제할 수 없습니다!')
                    exit()
            else:
                print('기존의 데이터베이스를 그대로 사용합니다.')
        else:
            print("데이터베이스 {}을 생성할 수 없습니다: ".format(DB_NAME), e.msg)
            exit()
    finally:
        cnx.database = DB_NAME

create_db()

for name, query in TABLES:
    try:
        print('테이블 {} 생성 중... '.format(name), end='')
        cur.execute(query)
    except conn.Error as e:
        if e.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('이미 존재합니다!')
        else:
            print('실패했습니다! ({})'.format(e.msg))
    else:
        print('OK!')

cur.close()
cnx.close()
