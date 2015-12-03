"""
    NSBoard

    from 20150904

    TODO:
        1. 예외 처리할 때, 에러 메시지 출력하는 것 지울 것.
        2. 각 페이지 제목(title) 제대로 표시할 것. (현재는 대부분 공백)
"""

from bottle import Bottle, redirect, request, run, static_file, template
from models import library
from config import SITE_NAME

import admin
import ajax

from math import ceil

# ----- GLOBALS ----- #
PER_PAGE = 20

# ----- ROUTING ----- #

app = Bottle()
app.mount('/a', admin.app)
app.mount('/ajax', ajax.app)


@app.route('/')
def main():
    try:
        lib = library.Library()
        new = lib.list_story_new_preview(1, 8)
        # hot = lib.list_hot(1, 5)
        title = SITE_NAME + ' - 즐거운 어른 소설 창고'

        return template('main', title=title, new=new)
    except Exception as e:
        raise e


@app.route('/b/<book_num:int>')
def show_book(book_num):
    # 책 정보 & 연재글 목록 보기
    this_page = request.query.p
    this_page = int(this_page) if this_page else 1
    lib = library.Library()
    info = lib.book_info(book_num)
    # info['keywords'] = _keyword_links(info['keywords'])
    story_list = lib.list_story_by_book(book_num, this_page, PER_PAGE)
    title = info['title'] + ' - ' + SITE_NAME
    return template('book_view', title=title, info=info, list=story_list)


@app.route('/b/<book_num:int>/<queue:int>')
def redirect_to_story(book_num, queue):
    try:
        lib = library.Library()
        story_num = lib.story_num(book_num, queue)
    except Exception as e:
        return template('popup', msg='해당 주소로 연결할 수 없습니다.')
    else:
        redirect('/s/{}'.format(story_num))


@app.route('/s/<story_num:int>')
def show_story(story_num):
    # TODO: 추천수 표시(?) + 추천 시 반응
    try:
        lib = library.Library()
        data = lib.story_view(story_num)
        data['story'] = data['story'].replace('\n', '<br />')
        # data['keywords'] = _keyword_links(data['keywords'])
        lib.view_count_add(story_num)
        title = data['title'] + ' - ' + SITE_NAME
        return template('story_view', title=title, data=data)
    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/new')
def list_new():
    # 새로 올라온 글 목록
    try:
        this_page = request.query.p
        this_page = int(this_page) if this_page else 1

        lib = library.Library()
        data = lib.list_story_new(this_page, PER_PAGE)

        # 페이지네이션
        total = lib.count_story_all()
        page = _pagination(this_page, total)
        title = '최근 작품 목록' + ' - ' + SITE_NAME
        return template('list_new', title=title, data=data, page=page)
    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/hot')
def list_hot():
    # 인기 작품 목록
    try:
        data = ''
        return
        title = '인기 작품 목록' + ' - ' + SITE_NAME
        return template('list_hot', title=title, data=data)
    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/keywords')
def list_keywords():
    # 키워드 목록
    try:
        lib = library.Library()
        # lib.clean_keywords()
        data = lib.list_keywords()

        title = '키워드 보기' + ' - ' + SITE_NAME
        return template('keywords.tpl', title=title, data=data)
    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/k/<keyword>')
def book_list_by_keyword(keyword):
    # 키워드별 작품 목록
    try:
        if not keyword:
            redirect('/keywords')
        this_page = request.query.p
        this_page = int(this_page) if this_page else 1

        lib = library.Library()
        data = lib.list_book_by_keyword(keyword, this_page, PER_PAGE)
        total = lib.count_book_by_keyword(keyword)
        page = _pagination(this_page, total)
        title = '"' +  keyword + '" 작품 목록' + ' - ' + SITE_NAME

        return template('list_keyword', title=title, data=data, keyword=keyword, page=page)
    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='static')


@app.error(404)
def error404(error):
    # TODO: 제대로 된 '존재하지 않는 페이지입니다.'를 만들 것.
    return '존재하지 않는 페이지입니다.'

@app.route('/test')
def test():
    header = request.headers

    return template('test', title="AJAX TEST", header=header)


# -----  END OF ROUTING ----- #


def _keyword_links(keywords):
    # 키워드 리스트를 받아, 링크 문자열 리스트를 만들어 반환
    result = []
    for kw in keywords:
        txt = '<a href="/k/{0}">{0}</a>'.format(kw)
        result.append(txt)
    return result


def _pagination(this_page, total):
    # 페이지내이션 데이터를 만들어서, 사전 형태로 반환
    PER_BLOCK = 5    # 페이지내이션 한 블럭에 표시할 숫자 갯수

    page = {}
    page['page'] = this_page
    page['total'] = ceil(total / PER_PAGE)
    page['start'] = (ceil(this_page / PER_BLOCK) - 1) * PER_BLOCK + 1
    page['end'] = page['start'] + (PER_BLOCK - 1)
    if page['end'] > page['total']:
        page['end'] = page['total']

    page['next'] = ceil(this_page / PER_BLOCK) * PER_BLOCK + 1
    page['next'] = page['next'] if page['next'] <= page['total'] else None
    page['prev'] = (ceil(this_page / PER_BLOCK) - 1) * PER_BLOCK
    page['prev'] = page['prev'] if page['prev'] > 1 else None

    return page



# ----- MAIN ----- #

if __name__ == '__main__':
    run(app=app, host='127.0.0.1', port=5000, debug=True, reloader=True)
