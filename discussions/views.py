from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Discussion, Thread

@login_required(login_url='/accounts/login/')
def index(request):
    discussions_list = Discussion.objects.all()
    context = {'discussions_list': discussions_list}
    return render(request, 'discussions/discussion_index.html', context)

@login_required(login_url='/accounts/login/')
def discussion_detail(request, discussion_id):
    discussion = get_object_or_404(Discussion, pk = discussion_id)
    threads_list = Thread.objects.filter(discussion=discussion)
    context = {'discussion': discussion, 'threads_list': threads_list}
    return render(request, 'discussions/discussion_detail.html', context)
