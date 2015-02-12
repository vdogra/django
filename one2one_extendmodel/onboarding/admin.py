from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from models import Seller

# Define an inline admin descriptor for Seller model
# which acts a bit like a singleton
class SellerInline(admin.StackedInline):
    model = Seller
    can_delete = False
    verbose_name_plural = 'Seller'

#Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (SellerInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)