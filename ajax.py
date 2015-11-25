"""
    ajax.py

    handling ajax requests
"""

from bottle import Bottle, request
from models import library

app = Bottle()

@app.route('/')
def ajax_main():
    return "HELLO"

@app.route('/get')
def ajax_get():
    return 'HELLO'

@app.route('/like')
def ajax_like():
    """
    추천 기록
    :return: 1. 성공, 2. 중복, 3. 잘못된 접근
    """
    ip = request.remote_addr
    story_num = request.query.s

    try:
        if ip and story_num:
            lib = library.Library()
            if lib.like_dupe_check(story_num, ip):
                return "2"
            lib.like_add(story_num, ip)
            return "1"
        else:
            return "3"
    except Exception as e:
        print("ERROR:", str(e))
        return 3