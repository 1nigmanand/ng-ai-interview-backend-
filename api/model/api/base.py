from enum import Enum
from typing import Generic, TypeVar, Optional, List
from pydantic import BaseModel
from datetime import datetime

T = TypeVar('T')

class ResponseCode(str, Enum):
    SUCCESS = "0"
    FAILED = "1"
    INVALID_PARAMS = "2"
    SYSTEM_ERROR = "500"

class Response(BaseModel, Generic[T]):
    code: str = ResponseCode.SUCCESS
    message: str = "success"
    data: Optional[T] = None

class PaginationMetadata(BaseModel):
    """Pagination metadata"""
    total_count: int
    page_size: int
    current_page: int
    total_pages: int
    has_next: bool
    has_previous: bool

class PaginationResponse(BaseModel, Generic[T]):
    """Response with pagination"""
    code: str = ResponseCode.SUCCESS
    message: str = "success"
    data: List[T] = []
    metadata: PaginationMetadata