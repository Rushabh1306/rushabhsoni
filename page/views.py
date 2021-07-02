from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Blog, Project, Presentation
# Create your views here.
def indexView(request):
    context = {}
    posts = Blog.objects.all().order_by('-date_posted')[:3]
    context['posts']=posts
    print(posts)

    projects = Project.objects.all().order_by('date_posted')[:3]
    context['projects']=projects
    # context={'projects':projects}
    print(projects)

    presentations = Presentation.objects.all().order_by('-date_posted')[:3]
    context['presentations']=presentations
    print(presentations)

    return render(request,'index.html',context)