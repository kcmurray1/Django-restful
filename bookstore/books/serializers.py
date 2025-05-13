from rest_framework import serializers
from books.models import Book, Comment, Rating
from django.db.models import Avg

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

# All fields in Book model should be serialized into a dictionary
class BookSerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="comment-record"
    )

    # dynamic attributes (not stored) into JSON
    book_type_text = serializers.SerializerMethodField(method_name='get_book_type_display_text')

    def get_book_type_display_text(self, instance):
        return instance.get_book_type_display()
    
    ratings = RatingSerializer(
        many=True,
        read_only=True
    )

    ratings_avg = serializers.SerializerMethodField(method_name='calc_rating_average')

    def calc_rating_average(self, instance):
        result = Rating.objects.filter(book=instance.id).aggregate(
            Avg('value')
        )

        return result['value__avg']

    # dynamic field
    popular = serializers.SerializerMethodField(method_name='is_popular')

    def is_popular(self, instance):
        avg = self.calc_rating_average(instance)
        return avg is not None and avg >= 3

    class Meta:
        model = Book
        fields = '__all__'
        # This removes book_type displaying when reading
        # but requires this argument when writing
        extra_kwargs = {
            'book_type' : {
                'write_only' : True
            }
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# NOTE: GEt requests follows this process to query a record(s) and render it as JSON or JSON array
# 1) gets record(s) from DB --> (serializer) --> Python dict --> (renderer) --> JSON object

# can be used like 
# 2) bs = BookSerializer(Book.book)
# can be used like bs.data = {"id": 5, "title": "learn java"}

# this can be used with a JSONRenderer
"""
from rest_framework.renderers import JSONRenderer
r = JSONRenderer()

x = r.render(bs.data)
print(x) -> b'{"id":5..} 

Decode like text = x.decode('UTF-8')
"""

# Serializing many objects
# 1) manyBooks = Book.objects.all()
# 2) bks_sr = BookSerializer(manyBooks, many=True)
# 3) bks_as_json = r.render(bks_sr.data)


# Deserializing from json string
# req_body = {"title" : "new book", "price": 2.99}

# from io import BytesIO
# req_bytes = req_body.encode('UTF-8')
# stream_book = BytesIO(req_bytes)
# from rest_framework.parsers import JSONParser
# p = JSONParser()
# parsed_book = p.parse(stream_book)