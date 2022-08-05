from dataclasses import dataclass
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from requests import post
from urllib3 import HTTPResponse
from blog.models import blogs , banner, catogry
from Learn.models import learn

data= {}
def homePage(request):
    bannerdata = banner.objects.all()
    blogdata = blogs.objects.all()[:6]
    blogsidedata = blogs.objects.all()[7:14]
    blogcatogry = catogry.objects.all()[:7]

    data= {
                'blogsdata':blogdata,
                'blogsidedata':blogsidedata,
                'bannerdata':bannerdata,
                'blogcatogry':blogcatogry,
    } 
    return render (request, 'templates/index.html', data )


def BlogPage(request,blogid):
    print (blogid)
    fullblog = blogs.objects.get(id=blogid)
    data = {
        'fullblogs': fullblog
    }
    return  render(request,'templates/blogs.html',data)

def learnpage(request,learnid):
    print (learnid)
    page = learn.objects.get(id=learnid)
    data= {
        'pages':page
    }
    return render (request, 'templates/learn.html',data)

def Mainblog(request):
    blogdata = blogs.objects.all()[:6]
    data={

        'blogsdata':blogdata,
    }

    return render(request, 'templates/Mainblog.html',data)     

def aboutus(request):
    return render( request, 'templates/aboutus.html')

def Community(request):

    return render(request, 'templates/Comunity.html')


def project( request):
    return render(request,'templates/projects.html') 

def Contact(request):

    return render(request, 'templates/Contactus.html')       

def thankuPage( request):
    if request.method =="GET":
        output= request.GET.get('output')

    return render( request, 'templates/thanku.html',{'output':output})


   
