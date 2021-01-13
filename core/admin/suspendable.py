"""
配合 core.models.suspendable SuspendableModel
"""

from django.contrib import admin

from .fields import merge_tuple_element, remove_tuple_element

suspend_readonly_fields = (
    'is_suspended',
    'suspended_user', 'suspended_datetime'
)

class SuspendableTabularInline(admin.TabularInline):

    def __init__(self, parent_model, admin_site):
        super().__init__(parent_model, admin_site)
        self.exclude = merge_tuple_element(self.exclude, suspend_readonly_fields)


    def delete_model(self, request, obj):
        obj.suspended_user = request.user
        obj.delete()


class SuspendableAdmin(admin.ModelAdmin):

    _suspend_fieldsets = (('停用紀錄', {'fields': (
        'is_suspended',
        ('suspended_user', 'suspended_datetime')
    )}),)


    def __init__(self, model, admin_site):
        self._origin_fieldsets = self.fieldsets
        self.readonly_fields = merge_tuple_element(
            self.readonly_fields,
            suspend_readonly_fields)
        super().__init__(model, admin_site)
        self._origin_fieldsets = self.fieldsets
    

    def delete_model(self, request, obj):
        obj.suspended_user = request.user
        obj.delete()


    def get_form(self, request, obj=None, change=False, **kwargs):
        if change:
            self.fieldsets = merge_tuple_element(self.fieldsets,
                self._suspend_fieldsets)
        else:
            self.fieldsets = remove_tuple_element(self.fieldsets,
                self._suspend_fieldsets)
        return super().get_form(request, obj, change, **kwargs)