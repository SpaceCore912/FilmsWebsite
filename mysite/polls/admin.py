from .models import Film,Group,Profile,Watchlist,Like,Genre,Category
from .forms import NameForm
from django.contrib import admin

admin.site.register(Film)
admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Watchlist)
admin.site.register(Like)
admin.site.register(Genre)
admin.site.register(Category)
# Register your models here.
