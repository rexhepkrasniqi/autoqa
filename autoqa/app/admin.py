from django.contrib import admin
from app.models import Step, Task, Action
import nested_admin
from app.workers import Worker

@admin.action(description="Do task")
def run_test(modeladmin, request, queryset):
    for obj in queryset:
        wk = Worker(obj)
        wk.run()
    


class StepInline(nested_admin.NestedStackedInline):
    model = Step
    sortable_field_name = "order"
    list_display = ("action", "target")


class ActionInline(nested_admin.NestedStackedInline):
    model = Action
    sortable_field_name = "description"


class TaskAdmin(nested_admin.NestedModelAdmin):
    inlines = [StepInline]
    actions = [run_test]
    readonly_fields = ("status", "message", "screenshot")
    list_display = ("name", "status")




admin.site.register(Task, TaskAdmin)
