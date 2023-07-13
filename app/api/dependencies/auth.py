from fastapi import Depends
from fastapi.security import APIKeyCookie

token = APIKeyCookie(name="token", auto_error=True)

DependsAuth = Depends(token)
