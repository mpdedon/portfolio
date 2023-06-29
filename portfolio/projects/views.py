from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.

def project_list(request):

    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_create(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')

    else:
        form = ProjectForm()
    return render(request, 'projects/project_create.html', {'form': form})

from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 5

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/project_create.html'
    form_class = ProjectForm

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/project_create.html'
    form_class = ProjectForm

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')