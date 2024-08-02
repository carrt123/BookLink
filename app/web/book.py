from helper import is_isbn_or_key
from booklink_book import BookLinkBooK
from . import web
import json

"""
@web.route('/bool/search')
def search():
    q = request.args['q']
    page = request.args['page']
    ....
"""
@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字
    :param page: 页码
    """
    isbn_or_key = is_isbn_or_key(q)
    bookLinkBook = BookLinkBooK()
    if isbn_or_key == "isbn":
        result = bookLinkBook.search_by_isbn(q)
    else:
        result = bookLinkBook.search_by_keyword(q)  # type(result) is dict
    # 等效 jsonfy(result)  jsonfy 由flask提供
    return json.dumps(result), 200, {'content-type': 'text/json'}
