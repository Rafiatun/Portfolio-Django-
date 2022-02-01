from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin



# Register your models here.
class SkillsAdmin(ImportExportModelAdmin):
    pass

class EducationAdmin(ImportExportModelAdmin):
    pass
class ExpAdmin(ImportExportModelAdmin):
    pass
class ProjectAdmin(ImportExportModelAdmin):
    pass

class PubAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Skills , SkillsAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience,ExpAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Publication,PubAdmin)

