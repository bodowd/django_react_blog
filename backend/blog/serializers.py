from rest_framework import serializers

from .models import BlogPost, Categories

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
        lookup_field = 'slug'

