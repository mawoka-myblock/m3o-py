from typing import Optional
from pydantic import BaseModel
from aiohttp import ClientSession
from m3o_py import GeneralException, UnknownError


class _User(BaseModel):
    id: str
    username: str
    email: str
    created: str
    updated: str
    verified: bool
    verificationDate: str
    profile: dict[str, str] | dict[None]


class _Session(BaseModel):
    id: str
    created: str
    expires: str
    userId: str


class _ListReturn(BaseModel):
    users: list[_User | None]


class _LoginResponse(BaseModel):
    session: _Session


class _ReadReturn(BaseModel):
    user: _User


class _ReadSessionReturn(BaseModel):
    session: _Session


class _VerifyTokenResponse(BaseModel):
    is_valid: bool
    message: Optional[str]
    session: _Session


class UserService:
    def __init__(self, token: str):
        self.token: str = token
        self.headers: dict = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    async def create(self, email: str, id: Optional[str], password: str, username: str) -> None:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/Create", json={"email": email, "id": id,
                                                                                "password": password,
                                                                                "username": username},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def delete(self, id: str) -> None:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/Create", json={"id": id},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def list(self, limit: int, offset: int) -> _ListReturn:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/List", json={"limit": limit, "offset": offset},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return _ListReturn(**await resp.json())
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def login(self, email: Optional[str], password: str, username: Optional[str]) -> _LoginResponse:
        """
        Either email or password must be provided.
        """
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/Login", json={"email": email, "password": password,
                                                                               "username": username},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return _LoginResponse(**await resp.json())
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def logout(self, session_id: str) -> None:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/Logout", json={"sessionId": session_id},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def read(self, email: Optional[str], id: Optional[str], username: Optional[str]) -> _ReadReturn:
        """
        Just one option has to be specified, returns GeneralException if no user found
        """
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/Read", json={"email": email, "id": id,
                                                                              "username": username},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return _ReadReturn(**await resp.json())
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def read_session(self, session_id: str) -> _ReadSessionReturn:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/ReadSession", json={"sessionId": session_id},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return _ReadSessionReturn(**await resp.json())
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def reset_password(self, code: str, confirm_password: Optional[str], password: str, email: str) -> None:
        """
        If confirm_password is None, it gets the value from password
        """
        if confirm_password is None:
            confirm_password = password
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/ResetPassword", json={"code": code,
                                                                                       "confirmPassword": confirm_password,
                                                                                       "password": password,
                                                                                       "email": email},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def send_magic_link(self, address: str, email: str, endpoint: str, from_name: str, subject: str,
                              text_content: str) -> None:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/SendMagicLink", json={"address": address,
                                                                                       "email": email,
                                                                                       "endpoint": endpoint,
                                                                                       "fromName": from_name,
                                                                                       "subject": subject,
                                                                                       "textContent": text_content},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def send_password_reset_email(self, email: str, from_name: str, subject: str, text_content: str,
                                        expiration: Optional[int] = 1800) -> None:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/SendPasswordResetEmail", json={"email": email,
                                                                                                "expiration": expiration,
                                                                                                "fromName": from_name,
                                                                                                "subject": subject,
                                                                                                "textContent": text_content},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def send_verification_email(self, email: str, failure_redirect_url: str, from_name: str, redirect_url: str,
                                      subject: str, text_content: str) -> None:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/SendVerificationEmail", json={"email": email,
                                                                                               "failureRedirectUrl": failure_redirect_url,
                                                                                               "fromName": from_name,
                                                                                               "redirectUrl": redirect_url,
                                                                                               "subject": subject,
                                                                                               "textContent": text_content},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def update(self, email: str, id: str, username: str, profile: Optional[dict[str, str]] = None) -> None:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/Update", json={"email": email,
                                                                                "id": id,
                                                                                "profile": profile,
                                                                                "username": username},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def update_password(self, confirm_password: Optional[str], new_password: str, old_password: str,
                             user_id: str) -> None:
        """
        If confirm_password is None, it gets the value from password
        """
        if confirm_password is None:
            confirm_password = new_password
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/UpdatePassword",
                                    json={"confirmPassword": confirm_password,
                                          "newPassword": new_password,
                                          "oldPassword": old_password,
                                          "userId": user_id},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def verify_email(self, token: str) -> None:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/VerifyEmail", json={"token": token},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())

    async def verify_token(self, token: str) -> _VerifyTokenResponse:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/user/VerifyToken", json={"token": token},
                                    headers=self.headers) as resp:
                if resp.status == 500 or resp.status == 400:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return _VerifyTokenResponse(**await resp.json())
                else:
                    raise UnknownError(f"Unknown error: {resp.status}", await resp.json())
