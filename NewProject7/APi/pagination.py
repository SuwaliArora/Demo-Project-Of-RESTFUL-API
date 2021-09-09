# locally define PageNumberPagination
from rest_framework.pagination import PageNumberPagination

class PageNumberpagination(PageNumberPagination):
    page_size = 5
    
