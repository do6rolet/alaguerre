from django.contrib import admin

from .models import Report

# admin.site.register(Report)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['created_by', 'created_at']