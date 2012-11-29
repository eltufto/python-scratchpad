from dummyjobfile.models import DummyJobFile, DummyTest, LocalOverride
from django.contrib import admin

class DummyTestsInline(admin.TabularInline):
    model = DummyJobFile.Dummy_tests.through
    extra = 1
    verbose_name = "Dummy Test"
    verbose_name_plural = "Dummy Tests"
    #fields = ('Dummy_test',)
    #raw_id_fields = ('Dummy_test',)

class DummyJobFileAdmin(admin.ModelAdmin):
    inlines = [DummyTestsInline]
    #fields = ('job_name', 'params')
    
class DummyTestAdmin(admin.ModelAdmin):
    list_display = ('specific_test', 'uri')
    
admin.site.register(DummyJobFile, DummyJobFileAdmin)
admin.site.register(DummyTest, DummyTestAdmin)
