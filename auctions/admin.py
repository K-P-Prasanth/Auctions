from django.contrib import admin
from .models import User,Category,create_listing,watchlist
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(create_listing)
admin.site.register(watchlist)