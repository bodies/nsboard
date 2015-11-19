"""
    ajax.py

    handling ajax requests
"""

from bottle import Bottle

app = Bottle()

@app.route('/')
def ajax_main():
    return "HELLO"

@app.route('/get')
def ajax_get():
    return 'HELLO'
