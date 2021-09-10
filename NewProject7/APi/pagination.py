# locally define PageNumberPagination, LimitoffsetPagination
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class PageNumberpagination(PageNumberPagination):
    page_size = 5
    
class LimitoffsetPagination(LimitOffsetPagination):
    default_limit = 5
    
class cursorpagination(CursorPagination):
    page_size = 3
    ordering = 'name' 
