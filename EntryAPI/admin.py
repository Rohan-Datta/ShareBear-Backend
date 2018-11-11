from django.contrib import admin
from EntryAPI.models import Entry

# Register your models here.
admin.site.register(Entry)

# Readonly Fields
class EntryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
