from django.shortcuts import render, redirect
from account.forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#login view
def login_view(request):
	context = {}

	user = request.user
	#if user already login, redirect to home
	if user.is_authenticated:
		redirect('home')

	if request.POST:
		#create login form
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			#authenticate user
			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
				return redirect('home')
	else:
		#display login form
		form = UserLoginForm()

	context['login_form'] = form

	return render(request, 'account/login.html', context)

#logout view
def logout_view(request):
	logout(request)
	return redirect('home')