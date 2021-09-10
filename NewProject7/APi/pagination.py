# locally define PageNumberPagination, LimitoffsetPagination
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class PageNumberpagination(PageNumberPagination):
    page_size = 5
    
class LimitoffsetPagination(LimitOffsetPagination):
    default_limit = 5
