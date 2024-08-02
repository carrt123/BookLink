from httper import Http
import json


class BookLinkBooK:
    isbn_url = "http://t.talelin.com/v2/book/isbn/{}"
    keyword_url = "http://t.talelin.com/v2/book/search?q={}&count={}&start={}"

    def search_by_isbn(self, isbn_id):
        self.isbn_url = self.isbn_url.format(isbn_id)
        result = Http.get(self.isbn_url)
        return result

    def search_by_keyword(self, keyword):
        self.keyword_url = self.keyword_url.format(keyword)
        result = Http.get(self.keyword_url)
        return result
