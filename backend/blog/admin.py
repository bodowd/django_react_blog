from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost

# Apply summernote to all TextField in model.
class BlogPostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    # so that slug field not present in Admin panel
    exclude = ('slug',)
    list_display = ('id', 'title', 'category', 'featured', 'date_created')

    # links you can click on to go into
    list_display_links = ('id', 'title')

    search_fields = ('title',)

    list_per_page = 25

    # the fields in the model that are going to have this typing widget is "content"
    summernote_fields = ('content', )

admin.site.register(BlogPost, BlogPostAdmin)