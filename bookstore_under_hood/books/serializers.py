from rest_framework import serializers
from books.models import Book, Comment


class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.FloatField()

    # create() is called whenever .save() is called on BookSerializer Objects
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    # update() is called whenever .save() is called on an existing object
    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.price = validated_data['price']
        instance.save()
        return instance