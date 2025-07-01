from django.contrib import admin
from .models import Tweet
# Register your models here.


admin.site.register(Tweet) # This will allow the Tweet model to be managed through the Django admin interface.