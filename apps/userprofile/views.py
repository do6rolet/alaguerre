from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm


def userprofile(request, username):
    user = get_object_or_404(User, username=username)
    reports = user.reports.all()
    for report in reports:
        likes = report.likes.filter(created_by_id=request.user.id)

        if likes.count() > 0:
            report.liked = True
        else:
            report.liked = False

    context = {
        'user': user,
        'reports': reports,
    }

    return render(request, 'userprofile/userprofile.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if form.is_valid():
            form.save()

            return redirect('userprofile', username=request.user.username)
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    context = {
        'user': request.user,
        'form': form,
    }

    return render(request, 'userprofile/edit_profile.html', context)


@login_required
def follow_reporter(request, username):
    user = get_object_or_404(User, username=username)

    request.user.userprofile.follows.add(user.userprofile)

    return redirect('userprofile', username=username)

@login_required
def unfollow_reporter(request, username):
    user = get_object_or_404(User, username=username)

    request.user.userprofile.follows.remove(user.userprofile)

    return redirect('userprofile', username=username)

def followers(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'userprofile/followers.html', {'user': user})

def follows(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'userprofile/follows.html', {'user': user})
