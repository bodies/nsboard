"""
    NSBoard

    from 20150904


    TODO:
        1. 예외 처리할 때, 에러 메시지 출력하는 것 지울 것.
"""

from bottle import Bottle, redirect, request, run, static_file, template
from models import library

import admin

# ----- ROUTING ----- #

app = Bottle()

app.mount('/a', admin.app)


@app.route('/')
def main():
    return template('main', title='')


@app.route('/b/<book_num:int>')
def show_book(book_num):
    lib = library.Library()
    info = lib.book_info(book_num)
    info['keywords'] = _keyword_links(info['keywords'])
    story_list = lib.story_list(book_num)
    return template('book_view', title='', info=info, list=story_list)


@app.route('/s/<story_num:int>')
def show_story(story_num):
    # TODO: IP 확인하고, 조회수 올리기
    try:
        lib = library.Library()
        data = lib.story(story_num)
        data['story'] = data['story'].replace('\n', '<br />')
        data['keywords'] = _keyword_links(data['keywords'])
        return template('story_view', title='', data=data)
    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/s/<story_num:int>/likes')
def likes_story(story_num):
    # 추천
    # TODO: IP 확인하고, 추천 처리
    pass


@app.route('/k/<keyword>')
def book_list_by_keyword(keyword):
    # 키워드별 작품 목록
    # TODO: 일반 게시판 목록처럼 페이지 구분을 해야 함.
    pass


@app.route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='static')


@app.error(404)
def error404(error):
    # TODO: 제대로 된 '존재하지 않는 페이지입니다.'를 만들 것.
    return '존재하지 않는 페이지입니다.'

# -----  END OF ROUTING ----- #


def _keyword_links(keywords):
    # 키워드 리스트를 받아, 링크 문자열 리스트를 만들어 반환
    result = []
    for kw in keywords:
        txt = '<a href="/t/{0}">{0}</a>'.format(kw)
        result.append(txt)
    return result

# ----- MAIN ----- #

if __name__ == '__main__':
    run(app=app, host='127.0.0.1', port=5000, debug=True, reloader=True)
