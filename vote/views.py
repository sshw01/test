from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Vote
from django.views.decorators.csrf import csrf_exempt

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_detail.html', {'project': project})

@csrf_exempt
def vote_all(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        for project in projects:
            score = request.POST.get(f'score_{project.id}')
            if score:
                Vote.objects.create(project=project, score=int(score))
                project.update_average_score()
        return redirect('results')

    return render(request, 'vote_all.html', {'projects': projects})

def results(request):
    projects = Project.objects.all().order_by('-avg_score')
    return render(request, 'results.html', {'projects': projects})


