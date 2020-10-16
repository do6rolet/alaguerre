from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Report, Like
from django.contrib.auth.models import User


@login_required
def inside(request):
    userids = [request.user.id]
    for reporter in request.user.userprofile.follows.all():
        userids.append(reporter.user.id)



    reports = Report.objects.filter(created_by_id__in=userids)

    for report in reports:
        likes = report.likes.filter(created_by_id=request.user.id)

        if likes.count() > 0:
            report.liked = True
        else:
            report.liked = False

    return render(request, 'inside/inside.html', {'reports': reports})


@login_required
def search_reporters(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        reporters = User.objects.filter(username__icontains=query)
    else:
        reporters = []

    context = {
        'query': query,
        'reporters': reporters
    }

    return render(request, 'inside/search_reporters.html', context)
