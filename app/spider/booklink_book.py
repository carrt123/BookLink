from app.utils.httper import Http
from flask import current_app


class BookLinkBooK:
    isbn_url = "http://t.talelin.com/v2/book/isbn/{}"
    keyword_url = "http://t.talelin.com/v2/book/search?q={}&count={}&start={}"

    def search_by_isbn(self, isbn_id: str):
        self.isbn_url = self.isbn_url.format(isbn_id)
        result = Http.get(self.isbn_url)
        return result

    def search_by_keyword(self, keyword: str, page: int = 1):
        self.keyword_url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = Http.get(self.keyword_url)
        return result

    @staticmethod
    def calculate_start(page: int) -> int:
        return (int(page)-1) * current_app.config['PER_PAGE']
