from django.contrib import admin
from blog.models import blogs , banner, catogry
class blogAdmin(admin.ModelAdmin):
    list_display = ('blog_date','blog_heading','blog_description','blog_image','blog_catagory',)
admin.site.register(blogs, blogAdmin)



class bannerAdmin(admin.ModelAdmin):
    list_display = ('bannerheading','banner_image',)
admin.site.register(banner,bannerAdmin)  


class catogryAdmin(admin.ModelAdmin):
    list_display = ('catogry_head','catogry_value')
admin.site.register(catogry,catogryAdmin)  

# Register your models here.

 