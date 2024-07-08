from django.shortcuts import (get_object_or_404,
                              render,
                              redirect,
                              )
from django.urls import reverse
from .models import Project
from .forms import ProjectForm

# Create your views here.
def ProjectList(request):
    project = Project.objects.all()

    context = {"project":project}
    return render(request,"Project/Project.html",context)

def create_view(request):

    context1 ={}

    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/ProjectList")
         
    context1['form']= form
    return render(request, "Project/create_view.html", context1)

def detail_view(request, id):
    context2 ={}

    context2["data"] = Project.objects.get(id = id)
         
    return render(request, "Project/detail_view.html", context2)

def update_view(request, id): 
    context3 ={}

    obj = get_object_or_404(Project, id = id)
 
    form = ProjectForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect("/ProjectList")
 
    # add form dictionary to context
    context3["form"] = form
 
    return render(request, "Project/update_view.html", context3)

def delete_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Project, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return redirect("/ProjectList")
 
    return render(request, "Project/delete_view.html", context)