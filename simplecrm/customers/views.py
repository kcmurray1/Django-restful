from rest_framework import generics, permissions
from customers.models import Customer, Contact
from customers.serializers import CustomerSerializer, ContactSerilizer
from customers.custom_permissions import IsCustomerOwnerPermission, IsOwnerPermission
from django.core import exceptions

class CustomerCollection(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    # This overrides the defualt behavior of 
    # queryset = Customer.objects.all()
    def get_queryset(self):
        auth_user = self.request.user
        return Customer.objects.filter(owner=auth_user)
    
    """
    We only want to set the owner as the self.request.user and not set the owner.
    This requires overriding the method perform_create

    Params:
        self: the request
        serializer: the serializer required to update the DB
    """
    def perform_create(self,serializer : CustomerSerializer):
        auth_user = self.request.user
        serializer.save(owner=auth_user)
        

    

class CustomerRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    permission_classes = [
        permissions.IsAuthenticated,
        # Authenticated user must be owner of the Customer Record
        IsOwnerPermission
    ]


class ContactCollection(generics.CreateAPIView):
    serializer_class = ContactSerilizer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def perform_create(self, serializer):
        customer_owner = serializer.validated_data['customer'].owner

        auth_user = self.request.user
        # Only the Customer record owner can update the contacts column
        if customer_owner == auth_user:
            serializer.save()
        else:
            raise exceptions.PermissionDenied

class ContactRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerilizer

    permission_classes = [
        permissions.IsAuthenticated,
        # authenticated user must be owner of the Contact record's Customer
        IsCustomerOwnerPermission
    ]