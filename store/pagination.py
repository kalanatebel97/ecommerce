from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class CategoryLimitPagination(LimitOffsetPagination):
    max_limit = 20
    default_limit = 20

class CategoryPageNumberPagination(PageNumberPagination):
    page_size = 10

class ProductLimitPagination(LimitOffsetPagination):
    max_limit = 10
    default_limit = 10

class ProductPageNumberPagination(PageNumberPagination):
    page_size = 10