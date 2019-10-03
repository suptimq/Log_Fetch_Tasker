from django.contrib import admin, auth
from log_fetcher.models import Fetcher
from django.utils.safestring import mark_safe


# Register the Admin classes for Fetcher using the decorator
class FetcherAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_name', 'start_date', 'end_date', 'task_status', 'display_path')
    ordering = ['-id']

    def display_path(self, obj):
        """Returns a string linked to download page."""
        display_file_path = obj.file_path.split('/')[-1]
        return mark_safe('<a href="/logs/{0}", target="_blank">{0}</a>'.format(
            display_file_path))

    display_path.short_description = 'log path'

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['app_name', 'start_date', 'end_date']
        return []


admin.site.register(Fetcher, FetcherAdmin)

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
