from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Student

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
 

# class PostSer(serializers.Serializer):

#     title = serializers.CharField(max_length=200 )
#     slug = serializers.SlugField(max_length=200 )
#     # author = serializers.ForeignKey(User, on_delete= .CASCADE,related_name='blog_posts')
#     updated_on = serializers.DateTimeField()
#     content = serializers.CharField(max_length=200)
#     created_on = serializers.DateTimeField( )
#     status = serializers.IntegerField()



class StudentSrl(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()

    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
