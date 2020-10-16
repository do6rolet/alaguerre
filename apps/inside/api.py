import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Report, Like


@login_required
def api_add_report(request):
    data = json.loads(request.body)
    body = data['body']

    report = Report.objects.create(body=body, created_by=request.user)

    return JsonResponse({'success': True})

@login_required
def api_add_like(request):
    data = json.loads(request.body)
    report_id = data['report_id']

    if not Like.objects.filter(report_id=report_id).filter(created_by=request.user).exists():
        like = Like.objects.create(report_id=report_id, created_by=request.user)


    return JsonResponse({'success': True})

