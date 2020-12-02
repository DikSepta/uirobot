from django.shortcuts import render, redirect
from account.forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
	context = {}

	user = request.user
	if user.is_authenticated:
		redirect('home')

	if request.POST:
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
				return redirect('home')
	else:
		form = UserLoginForm()

	context['login_form'] = form

	return render(request, 'account/login.html', context)

def logout_view(request):
	logout(request)
	return redirect('home')