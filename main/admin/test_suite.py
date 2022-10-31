from django.contrib import admin
from nested_admin.nested import NestedModelAdmin

from main.models import TestSuite


@admin.register(TestSuite)
class TestAdmin(NestedModelAdmin):
    pass
