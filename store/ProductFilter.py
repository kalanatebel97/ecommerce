from rest_framework import filters

class ProductSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('category'):
            return ['category_id__title']
        elif request.query_params.get('subcategory'):
            return ['subcategory_title']
        else:
            return ['name','description','category_id__title']
