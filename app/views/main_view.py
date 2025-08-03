from django.shortcuts import render, redirect
from ..models import Service, Skill, Project, About, Contact

def home(request):
    return render(request,'main/home.html')


def about(request):
    return render(request,'main/about.html')

def add_project(request):
    errors={}
    if request.method == 'POST':
        title=request.POST.get('title')
        image=request.FILES.get('image')
        description= request.POST.get('description')

        if not title:
            errors['title']= 'Title is required'
        if not image:
            errors['image']='Title is not required'
        if not description:
            errors['description']='Description is required'
        if not errors:
            project_data=Project.objects.create(
                title=title,
                image=image,
                description=description
            )
            project_data.save()
            return redirect('project')
    return render(request, 'add/add_project.html',{'error':errors})


def project(request):
    project_data= Project.objects.all()
    return render(request,'main/project.html',{'data':project_data})


def single_project(request,id):
     project_data=Project.objects.get(id=id)
     return render(request,'single/single_project.html',{'data':project_data})

def edit_project(request,id):
    project_data=Project.objects.get(id=id)
    if request.method== "POST":
        project_data.title=request.POST.get('title')
        project_data.description=request.POST.get('description')
        project_data.image=request.FILES.get('image')
        project_data.save()
        return redirect('single_project.html')
    return render(request,'edit/edit_project.html',{"data":project_data})


def contact(request):
    return render(request,'main/contact.html')


def skill(request):
    return render(request,'main/skill.html')


def service(request):
    return render(request, 'main/service.html')

def edit_project(request):
    return render(request,'edit/edit_project.html')
