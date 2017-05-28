from django.shortcuts import render
from data.models import *
# Create your views here.
def home(request):
    """ Web landing page url: '/'
    """
    repo_list = []
    repo_objs  = Repositories.objects.all()
    for repo in repo_objs:
        images = repo.built_by.all()
        for img in images:
            print img.image
    context = {'repo_objs': repo_objs}
    return render(request, 'data/home.html', context)

