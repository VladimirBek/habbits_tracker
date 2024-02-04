from rest_framework.pagination import PageNumberPagination


class CustomPaginationClass(PageNumberPagination):
    """
    Pagination class for HabitsListView

    page_size: Count of objects on one-page
    page_size_query_param: Parameter for specifying the number of objects on one page by get request
    max_page_size: Maximum number of objects on one page
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
