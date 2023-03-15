from fastapi import APIRouter, HTTPException, Header
from jose import  jwt, JWTError

from core.models import Post
from core.schemas import PostDetail, PostCreateForm

from core.settings import EXPIRE_JWT_TOKEN, TOKEN_TYPE, ALGORITHM, SECRET_KEY


post_router = APIRouter(prefix='/post')