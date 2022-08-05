"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('Learn/<learnid>',views.learnpage,name='learn'),
    path('Blogs/<blogid>',views.BlogPage, name='Blog'),
    path('Mainblog', views.Mainblog, name= 'mainblog'),
    path('Community',views.Community, name='comunity'),
    path('Contact-Us',views.Contact, name='Contact'),
    path('projects',views.project, name='project'),
    path('thanku', views.thankuPage, name= 'thanku'),
]
   
    
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 