from django.contrib import admin
from .models import Contact, NameWoman, NameMan

admin.site.register(Contact)
admin.site.register(NameMan)
admin.site.register(NameWoman)
