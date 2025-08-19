from django.contrib import admin
from .models import CustomerModel

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'fullname',
        'email',
        'mobile',
        'address',
        'created_at',
        'updated_at',
    ]
    list_display_links = [
        'fullname',
        'email',
        'mobile',
        'address',
        'created_at',
        'updated_at',
    ]

admin.site.register(CustomerModel, CustomerAdmin)