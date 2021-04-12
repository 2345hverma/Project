from django.contrib import admin

# Register your models here.
from reminders.models import Subjects, Reminders

admin.site.register(Subjects)
admin.site.register(Reminders)