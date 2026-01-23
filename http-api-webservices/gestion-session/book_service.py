from http_session import HttpSession

class BookService:
    def __init__(self, http_session: HttpSession):
        self.http = http_session

    def list_books(self):
        return self.http.get("/api/books")