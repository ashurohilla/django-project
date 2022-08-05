from django.contrib import admin
from Learn.models import learn
class learnAdmin(admin.ModelAdmin):
    list_display = ('Learn_Head','Learn_heading','Learn_description')
admin.site.register(learn, learnAdmin)


# Register your models here.
