from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    WORLD = 'world'
    ENVIRONMENT = 'environment'
    TECHNOLOGY = 'technology'
    DESIGN = 'design'
    CULTURE = 'culture'
    BUSINESS = 'business'
    POLITICS = 'politics'
    OPINION = 'opinion'
    SCIENCE = 'science'
    HEALTH = 'health'
    STYLE = 'style'
    TRAVEL = 'travel' 

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.WORLD)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    # override the save method
    # automatically make the slug so that it can use the same titles but adds a number to the end to make slug unique
    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        # find if any slugs are the same as the, we want to rename to make every slug unique
        # count how many there are
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        # while queryset is not null
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            # check again to see if this slug exists. if not, exit while loop
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                # set the current featured object to false so that we can replace it with the new featured one
                temp = BlogPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass
        
        # finally save
        super(BlogPost, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

