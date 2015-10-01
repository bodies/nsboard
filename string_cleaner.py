'''
    string_clenaer.py

    사용자 입력값에서 태그, 공백 등을 제거
'''

import re
TAG_RE = re.compile(r'<[^>]+>')


def clean(string):
    # 태그 & 모든 공백 제거
    return remove_tags(string).replace(' ', '')


def remove_tags(string):
    # 태그 & 앞뒤 공백 제게
    return TAG_RE.sub('', string).strip()
