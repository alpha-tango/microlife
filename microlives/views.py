from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from microlives.models import MicroLife, Exposure, SiteUser
from django.contrib.auth.models import User

def index(request):
    context = {}
    return render(request, 'microlives/index.html', context)

class UserProfileView(DetailView):
    model = User
    slug_field = "username"
    template_name = "microlives/user_profile.html"
