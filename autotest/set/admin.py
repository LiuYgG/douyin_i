from django.contrib import admin
from set.models import Set
# Register your models here.

class setAdmin(admin.ModelAdmin):
    list_display = ['setname', 'setvalue', 'id']

admin.site.register(Set)
