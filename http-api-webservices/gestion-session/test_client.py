from http_session import HttpSession
from book_service import BookService

BASE_URL = "http://127.0.0.1:8000"
ACCESS_TOKEN = "expired-token"
REFRESH_TOKEN = "fake-refresh-token"

if __name__ == "__main__":
    session = HttpSession(
        base_url=BASE_URL,
        access_token=ACCESS_TOKEN,
        refresh_token=REFRESH_TOKEN,
    )

    books = BookService(session).list_books()
    print(books)