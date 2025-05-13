from rest_framework import serializers
from customers.models import Customer, Contact

class ContactSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    contacts = ContactSerilizer(
        many=True,
        read_only=True
    )
    
    class Meta:
        model = Customer
        fields = ["id", "name", "industry", "contacts"]
    