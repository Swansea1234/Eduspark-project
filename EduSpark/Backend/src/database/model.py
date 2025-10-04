from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class User(BaseModel):
    id: str
    username: str
    email: str
    is_admin: bool = False

class Lesson(BaseModel):
    title: str
    content: str
    owner_id: str
    is_public: bool = False

class LessonCreate(BaseModel):
    title: str
    content: str
    is_public: Optional[bool] = False

class LessonInDB(Lesson):
    id: str

class LessonUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_public: Optional[bool] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class LessonPrompt(BaseModel):
    user_query: str
    context: Optional[str] = None
