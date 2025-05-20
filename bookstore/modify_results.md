# Pagination
In the project file settings.py add
```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.LimitOffsetPagination',
}
```
We can specify the default limit and offset like
```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 4,
}
```
**NOTE** this does not enforce the page size, users could simply adjust the url to use limit=100
## Limiting pagination
We can create a custome class and adjust the REST_FRAMEWORK config to use it

```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS' : books.custom_pagination.LimitOffsetPaginationWithUpperBound',
    'PAGE_SIZE': 4,
}
```
# Sorting
Adding the config
```
REST_FRAMEWORK = {
   'DEFAULT_FILTER_BACKENDS' : (
       'rest_framework.filters.OrderingFilter',
   )
}
```
Allows us to order results like 
http://127.0.0.1:8000/api/books?ordering=price where the filter name is the column of a model. In this case the book model has the columns 'title', 'price', and 'description'

## Sorting by multiple filters
we can sort by multiple fields by using a comma. This example will sort by price and then by title when the prices are the same.
http://127.0.0.1:8000/api/books?ordering=price,title

## Limiting filters
We can specify what fields we want to allow for sorting by adjusting the views.py
with
```python
order_fields = ('price',) #insert sortable fields as a tuple
```
# Search
We can add a sorting configuration to settings.py
```python
REST_FRAMEWORK = {
   'DEFAULT_FILTER_BACKENDS' : (
       'rest_framework.filters.OrderingFilter',
       'rest_framework.filters.SearchFilter',
   )
}
```
This allows users to search information like
```
http://127.0.0.1:8000/api/books?search=dragon
```
However, by default this search filter will search all fields
we can specify what fields to use by
```python
search_fields = ('title',)
```