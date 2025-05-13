from django.urls import path
from customers.views import CustomerCollection, CustomerRecord, ContactCollection, ContactRecord

urlpatterns = [
    path('customers', CustomerCollection.as_view()),
    path('customers/<int:pk>', CustomerRecord.as_view()),
    path('contacts', ContactCollection.as_view()),
    path('contacts/<int:pk>', ContactRecord.as_view())

]