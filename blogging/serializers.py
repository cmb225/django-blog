from django.contrib.auth.models import User
from blogging import models
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = ['title', 
                  'text',
                  'created_date',
                  'modified_date',
                  'published_date']
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name', 
                  'description',
                  'posts']     
