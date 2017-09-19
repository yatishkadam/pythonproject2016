
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def lists(request):
	users = User.objects.order_by("username")
	return render(request, 'user/user_list.html', {"users":users})

@login_required
def profile(request, user):
	users = User.objects.all()
	for i in users:
		if i.username == user:
			return render(request, 'user/user_profile.html', {"user": i})