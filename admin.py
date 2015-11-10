"""
    admin.py
"""

from bottle import Bottle, redirect, request, template, static_file, BaseRequest
from beaker.middleware import SessionMiddleware
from models import library
from string_cleaner import *

session_opts = {
    'sesstion.type': 'memory',
    # 'session.cookie_expires': 3000,
    'session.auto': True
}

BaseRequest.MEMFILE_MAX = 1024 * 1024
SITE_NAME = '꿀단지 (관리)'

# ----- ROUTING ----- #

app = Bottle()


def check_auth(func):
    # 로그인 확인용 데코레이터
    # 인자로 주어진 함수에서 예외가 발생하면 여기 걸린다!
    # 로그인 여부를 예외로 처리하지 말 것!
    def checker(*args, **kwargs):
        return func(*args, **kwargs)  # 디버깅용

        s = request.environ.get('beaker.session')
        if 'remote_addr' in s and s['remote_addr'] == request.environ.get('REMOTE_ADDR'):
            return func(*args, **kwargs)
        else:
            return template('popup', msg='잘못된 접근입니다.', dest='/a/login')
    return checker


@app.route('/')
@check_auth
def admin_main():
    title = SITE_NAME
    return template('admin_main', title=title)


@app.route('/login')
def login_form():
    title = '로그인 - ' + SITE_NAME
    return template('login', title=title, action='login')


@app.route('/login', method='POST')
def do_login():
    try:
        user_id = request.forms.get('user_id')
        passwd = request.forms.get('passwd')

        if not user_id or not passwd:
            raise Exception('잘못된 접근입니다.')

        if user_id == 'asdf' and passwd == '1234':
            s = request.environ.get('beaker.session')
            s['remote_addr'] = request.environ.get('REMOTE_ADDR')
            s.save()
            return template('popup', msg='로그인 성공: {}'.format(s['remote_addr']), dest='.')
        else:
            return template('popup', msg='로그인 실패', dest='login')

    except Exception as e:
        return template('popup', msg=str(e), dest='login')


@app.route('/logout')
def do_logout():
    s = request.environ.get('beaker.session')
    s.delete()
    return template('popup', msg='로그아웃되었습니다.', dest='/')


@app.route('/book_list')
@check_auth
def show_book_list():
    try:
        lib = library.Library()
        result = lib.book_list()
        title = '작품 목록 - ' + SITE_NAME
        return template('admin_book_list', title=title, data=result)
    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/new_book')
@check_auth
def new_book_form():
    title = '새 작품 등록 - ' + SITE_NAME
    return template('admin_new_book', title=title, action='/a/new_book')


@app.route('/new_book', method='post')
@app.route('/b/<book_num:int>/mod', method='post')
@check_auth
def save_new_book(book_num=None):
    try:
        title = remove_tags(request.forms.getunicode('title'))
        series_raw = request.forms.get('is_series').strip()
        public_raw = request.forms.get('is_public').strip()
        complete_raw = request.forms.get('is_complete', default='').strip()
        keywords_raw = clean(request.forms.getunicode('keywords'))
        intro = remove_tags(request.forms.getunicode('intro'))

        if not title or not series_raw or not public_raw:
            raise Exception('작품 정보가 잘못 입력되었습니다.')

        # 데이터 정리
        series = 1 if series_raw == 'True' else 0
        public = 1 if public_raw == 'True' else 0
        complete = 1 if complete_raw == 'True' else 0
        keywords = [tmp.replace(' ', '') for tmp in keywords_raw.split(',')]

        lib = library.Library()

        if not book_num:
            book_num = lib.new_book(title, series, public, complete, keywords, intro)
            if not book_num:
                raise Exception('새 작품을 등록할 수 없습니다. 잠시 후 다시 시도해주세요.')
            msg = '<{}>이 새 작품으로 등록되었습니다.'.format(title)
        else:
            lib.modify_book(book_num, title, series, public, complete, keywords, intro)
            msg = '<{}>의 작품 정보를 수정했습니다.'.format(title)

        return template('popup', msg=msg, dest='/a/b/{}'.format(book_num))

    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/b/<book_num:int>/mod')
@check_auth
def modify_book(book_num):
    try:
        lib = library.Library()
        book_info = lib.book_info(book_num)
        mod = True
        title = '<' + book_info['title'] + '> 정보 수정 - ' + SITE_NAME
        return template('admin_new_book', title=title, data=book_info, mod=mod,
                        action='/a/b/{}/mod'.format(book_num))
    except Exception as e:
        print('MODIFY_BOOK:', str(e))
        return template('popup', msg='작품 정보를 수정할 수 없습니다.')


@app.route('/b/<book_num:int>/list')
@check_auth
def story_list(book_num):
    try:
        page = request.query.get('p', 1)
        lib = library.Library()
        data = lib.story_list(book_num, page)
        book_title = lib.book_name(book_num)
        title = book_title + ' 연재 목록 - ' + SITE_NAME

        return template('admin_story_list', title=title, book_title=book_title,
                        book_num=book_num, data=data)
    except Exception as e:
        msg = 'STORY_LIST: {}'.format(str(e))
        return template('popup', msg=msg)


@app.route('/b/<book_num:int>')
@check_auth
def book_info(book_num):
    try:
        lib = library.Library()
        data = lib.book_info(book_num)
        title = data['title'] + ' - ' + SITE_NAME
        return template('admin_book_info', title=title, data=data)
    except Exception as e:
        return template('popup', msg='작품 정보를 출력할 수 없습니다.\\n{}'.format(str(e)))


@app.route('/b/<book_num:int>/write_story')
@check_auth
def write_story(book_num):
    try:
        # TODO: 글쓰기 폼 출력, 제목과 몇번째 연재인지 상단에 출력
        lib = library.Library()
        data = lib.book_info(book_num)
        data['queue_num'] = data['story_count'] + 1
        data['book_title'] = data['title']
        data['title'] = data['book_title'] + ' ' + str(data['queue_num']) + '부'
        title = '"' + data['book_title'] + '" 연재 - ' + SITE_NAME

        return template('admin_write_story', title=title, data=data,
                        action='/a/b/{}/write_story'.format(book_num))

    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/b/<book_num:int>/write_story', method='post')
@check_auth
def save_story(book_num):
    try:
        # TODO: 연재글을 받아서, 정리하고, 저장
        # 연재 순서는 pub_date로 지정된다.
        # 혹시 연재 순서를 잘못 올렸을 때는 그 이후 연재글을 다 지우고 새로 입력해야..

        print('SAVE_STORY')
        queue = clean(request.forms.get('queue'))
        print('QUEUE', queue)
        title = remove_tags(request.forms.getunicode('title'))
        story = remove_tags(request.forms.getunicode('story'))
        public_raw = request.forms.get('is_public').strip()
        public = 1 if public_raw == 'True' else 0

        lib = library.Library()
        if lib.queue_dupe_check(book_num, queue):
            raise Exception('{}회가 이미 존재합니다.'.format(queue))
        print("SAVE_STORY")
        story_num = lib.new_story(book_num, queue, title, story, public)

        print('새로운 글 번호:', story_num)

        return template('popup', msg='새로운 글이 등록되었습니다.',
                        dest='/a/b/{}'.format(book_num))
    except Exception as e:
        return template('popup', msg='새 글을 등록할 수 없습니다.\\n{}'.format(str(e)))


@app.route('/s/<story_num:int>/mod', method='post')
@check_auth
def update_story(story_num):
    try:
        queue = clean(request.forms.get('queue'))
        title = remove_tags(request.forms.getunicode('title'))
        story = remove_tags(request.forms.getunicode('story'))
        public_raw = request.forms.get('is_public').strip()
        public = 1 if public_raw == 'True' else 0

        lib = library.Library()
        book_num = lib.book_num(story_num)

        if lib.queue_dupe_check(book_num, queue) and not lib.match_queue_num(story_num, queue):
            # 1. 작품 내 회차가 이미 존재하고,
            # 2. 기존의 회차 번호를 그냥 사용하는 것이 아닐 경우,
            raise Exception('회차 번호가 다른 글과 겹칩니다!')
        else:
            # 회차 번호가 안 겹치거나, 변경하지 않았을 경우
            lib.modify_story(story_num, queue, title, story, public)

        return template('popup', msg='{}을 변경했습니다.'.format(title),
                        dest='/a/s/{}'.format(story_num))
    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/s/<story_num:int>')
@check_auth
def show_story(story_num):
    try:
        lib = library.Library()
        data = lib.story(story_num)
        data['story'] = data['story'].replace('\n', '<br />')
        return template('admin_show_story', title='', data=data)
    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/s/<story_num:int>/mod')
@check_auth
def modify_story(story_num):
    try:
        lib = library.Library()
        data = lib.story(story_num)
        mod = True
        return template('admin_write_story', title='', data=data, mod=mod,
                        action='/a/s/{}/mod'.format(story_num))
    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/backup')
@check_auth
def backup():
    import os
    from config_db import DB_USER, DB_PASSWORD, DB_NAME
    import time
    str_date = 'nsboard_{}'.format(time.strftime('%Y%m%d%H%M%S'))
    os.system('mysqldump -u{} -p{} {} > {}.sql'.format(DB_USER,
              DB_PASSWORD, DB_NAME, str_date))
    os.system('tar zcf nsboard.tar.gz {}.sql'.format(str_date))
    os.system('rm {}.sql'.format(str_date))
    os.system('mv nsboard.tar.gz ./tmp/{}.tar.gz'.format(str_date))
    return static_file('{}.tar.gz'.format(str_date), root='tmp')


@app.route('/test')
def test():
    return "TEST!"

app = SessionMiddleware(app, session_opts)
