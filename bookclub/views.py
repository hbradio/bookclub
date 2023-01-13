from django.shortcuts import redirect

from discussions import views as discussion_views

def index(request):
    return redirect(discussion_views.index)