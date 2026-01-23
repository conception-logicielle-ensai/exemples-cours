from fastapi import APIRouter, HTTPException, Header, status
from typing import Final

from api.models.auth import RefreshRequest
from api.data.books import BOOKS

router = APIRouter()

# ======================================================
# Constantes
# ======================================================

AUTH_HEADER_PREFIX: Final[str] = "Bearer"

VALID_REFRESH_TOKEN: Final[str] = "fake-refresh-token"
VALID_ACCESS_TOKEN: Final[str] = "new-access-token"

# ======================================================
# Helpers
# ======================================================


def build_bearer_token(token: str) -> str:
    return f"{AUTH_HEADER_PREFIX} {token}"


def validate_access_token(authorization: str | None) -> None:
    expected = build_bearer_token(VALID_ACCESS_TOKEN)

    if authorization != expected:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Expired token",
        )


def validate_refresh_token(payload: RefreshRequest) -> None:

    if payload.refresh_token != VALID_REFRESH_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )


# ======================================================
# Endpoints
# ======================================================


@router.post("/auth/refresh")
def refresh_token(payload: RefreshRequest):

    validate_refresh_token(payload)

    return {"access_token": VALID_ACCESS_TOKEN}


@router.get("/api/books")
def list_books(authorization: str | None = Header(default=None)):

    validate_access_token(authorization)

    return BOOKS