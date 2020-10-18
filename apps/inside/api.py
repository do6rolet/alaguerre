import json
import re # regular expressons

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Report, Like
from apps.notification.utilities import create_notification


@login_required
def api_add_report(request):
    data = json.loads(request.body)
    body = data['body']

    report = Report.objects.create(body=body, created_by=request.user)

    results = re.findall("(^|[^@\w])@(\w{1,20})", body)
    for result in results:
        result = result[1]

        print(result)

        if User.objects.filter(username=result).exists() and result != request.user.username:
            create_notification(request, User.objects.get(username=result), 'mention')

    return JsonResponse({'success': True})

@login_required
def api_add_like(request):
    data = json.loads(request.body)
    report_id = data['report_id']

    if not Like.objects.filter(report_id=report_id).filter(created_by=request.user).exists():
        like = Like.objects.create(report_id=report_id, created_by=request.user)
        report = Report.objects.get(pk=report_id)
        create_notification(request, report.created_by, 'like')


    return JsonResponse({'success': True})

