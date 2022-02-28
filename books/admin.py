from django.contrib import admin

from .models import Books
from rest_framework.authtoken.admin import TokenAdmin

admin.site.register(Books)


TokenAdmin.raw_id_fields = ['user']