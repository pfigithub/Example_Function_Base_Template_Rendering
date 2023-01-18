from django.views.generic import TemplateView
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required


class Home(TemplateView):
    template_name = 'base.html'





# def login_view(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = AuthenticationForm(request=request, data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data.get('username')
#                 email = form.cleaned_data.get('email')
#                 password = form.cleaned_data.get('password')
#                 user = authenticate(
#                     request,email=email, username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     return redirect('/')

#         form = AuthenticationForm()
#         context = {'form': form}
#         return render(request, 'accounts/login.html', context)
#     else:
#         return redirect('/')


# @login_required
# def logout_view(req):
#     logout(req)
#     return redirect('home')


# def signup_view(req):
#     if not req.user.is_authenticated:
#         if req.method == 'POST':
#             form = UserCreationForm(req.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/')
#         form = UserCreationForm()
#         context = {'form': form}
#         return render(req, 'accounts/signup.html', context)
#     else:
#         return redirect('/')

