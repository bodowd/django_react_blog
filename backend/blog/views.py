from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BlogPost, Categories
from .serializers import BlogPostSerializer

class BlogPostListView(ListAPIView):
    # order by the latest blog post
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    # lookup_field defaults to 'pk'
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostDetailView(RetrieveAPIView):
    # order by the latest blog post
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    # default lookup field is pk
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostFeaturedView(ListAPIView):
    # order by the latest blog post
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostCategoryView(APIView):
    # serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        """
        post request will look for the category we're sending
        """
        data = self.request.data
        category = data['category']
        # we want the latest posts, then we filter by cateogry
        queryset = BlogPost.objects.order_by('-date_created').filter(category__iexact=category)
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)

