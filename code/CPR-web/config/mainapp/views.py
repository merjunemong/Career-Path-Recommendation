from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm, JobForm, ListForm
from .resume_to_skills import getSkillsFromResume
from .CPR_GraphDB import *
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'uploadPDF':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_file = request.FILES['file']
                fs = FileSystemStorage()
                filename = fs.save(uploaded_file.name, uploaded_file)
                file_url = fs.url(filename)

                skills = getSkillsFromResume(fs.path(filename))
                request.session['skills'] = skills
            return redirect('projects')
    else:
        form = UploadFileForm()
    skills = request.session.pop('skills', None)
    return render(request, 'projects.html', {'form':form, 'skills':skills})

def projects_result(request):
    if request.method == 'POST':
        jobs = None
        body = json.loads(request.body)
        form = ListForm(body)
        if form.is_valid():
            skills = body.get('skills')
            jobs = getJob(skills)
            request.session['jobs'] = jobs
        return render(request, 'projects-result.html', {'form':form, 'jobs':jobs})
    else:
        form = ListForm()
    jobs = request.session.pop('jobs', None)
    return render(request, 'projects-result.html', {'form':form, 'jobs':jobs})


def resume(request):
    return render(request, 'resume.html')

def draw_graph(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        form = JobForm(body)
        if form.is_valid():
            job = body.get('job')
            skills = getSkills(job)
            request.session['job_name'] = job
            request.session['skills'] = skills
            return render(request, 'graph/graph.html', {'job_name': job, 'skills': skills})
    else:
        form = JobForm()
    job = request.session.pop('job_name', None)
    skills = request.session.pop('skills', None)
    return render(request, 'graph/graph.html', {'job_name': job, 'skills': skills})

def upgrade_graph(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        form = JobForm(body)
        if form.is_valid():
            job = body.get('job')
            skills = getSkills(job)
            request.session['job_name'] = job
            request.session['skills'] = skills
            return render(request, 'graph/graph.html', {'job_name': job, 'skills': skills})
    else:
        form = JobForm()
    job = request.session.pop('job_name', None)
    skills = request.session.pop('skills', None)
    return render(request, 'graph/graph.html', {'job_name': job, 'skills': skills})