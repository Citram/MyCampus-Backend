from django.contrib import admin

# added code to edit events and users in the admin interface
from .models import *

admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(RegularUser)
admin.site.register(Organization)