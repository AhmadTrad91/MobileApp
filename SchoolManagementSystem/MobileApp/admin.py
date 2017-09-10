from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from MobileApp.models import *

admin.site.register(Classes)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Agenda)
admin.site.register(Notifications)