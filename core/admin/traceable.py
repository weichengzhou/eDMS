"""
配合 core.models.traceable TraceableModel
"""

from django.contrib import admin

from .fields import merge_tuple_element, remove_tuple_element

trace_readonly_fields = (
    'created_user', 'created_datetime',
    'updated_user', 'updated_datetime'
)


class TraceableTabularInline(admin.TabularInline):

    def __init__(self, parent_model, admin_site):
        super().__init__(parent_model, admin_site)
        self.exclude = merge_tuple_element(self.exclude, trace_readonly_fields)


    def save_model(self, request, obj, form, change):
        obj.updated_user = request.user
        if not change:
            obj.created_user = request.user
        super().save_model(request, obj, form, change)


class TraceableAdmin(admin.ModelAdmin):

    _trace_fieldsets = (('歷史紀錄', {'fields': (
        ('created_user', 'created_datetime'),
        ('updated_user', 'updated_datetime')
    )}),)


    def __init__(self, model, admin_site):
        self.readonly_fields = merge_tuple_element(
            self.readonly_fields,
            trace_readonly_fields)
        super().__init__(model, admin_site)
        self._origin_fieldsets = self.fieldsets
    

    def save_model(self, request, obj, form, change):
        obj.updated_user = request.user
        if not change:
            obj.created_user = request.user
        super().save_model(request, obj, form, change)
    

    def get_form(self, request, obj=None, change=False, **kwargs):
        if change:
            self.fieldsets = merge_tuple_element(self.fieldsets,
                self._trace_fieldsets)
        else:
            self.fieldsets = remove_tuple_element(self.fieldsets,
                self._trace_fieldsets)
        return super().get_form(request, obj, change, **kwargs)