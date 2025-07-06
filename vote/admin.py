from django.contrib import admin

from .models import Project, Vote

admin.site.register(Vote)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'avg_score', 'created_at')
    ordering = ['-avg_score'] 
