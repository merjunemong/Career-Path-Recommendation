from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from .resume_to_skills import getSkills

# Create your views here.

def index(request):
    return render(request, 'index.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)

            skills = getSkills(fs.path(filename))
            return render(request, 'uploadFile/upload_success.html', {'skills': skills})
    else:
        form = UploadFileForm()
    return render(request, 'uploadFile/upload.html', {'form': form})