from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import UserModel
from .forms import UserCreationForm


# Create your views here.
def createUser(request):
    formset = UserCreationForm()
    if request.method == 'POST':
        formset = UserCreationForm(request.POST)
        if formset.is_valid():
            user = UserModel.objects.filter(email=formset.data['email']).exists()
            if user is False:
                send_mail(
                    subject='Lushlyrics: Account Creation',
                    message= f"Dear {formset.data['first_name']} {formset.data['last_name']},\n\nCongratulations! You have successfully created an account on Lushlyrics.\n\nRegards,\Lushlyrics\nhttps://lushlyrics.vercel.app",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[formset.data['email']]
                )
                formset.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
            else:
                messages.error(request, 'User already exist!')
        else:
            messages.error(request, formset.errors)
    return render(request, 'registration/signup.html', {'formset': formset})


def loginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = authenticate(request, email=email.lower(), password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'email or password is incorrect!')
        except:
            messages.error(request, 'user does not exist!')       
    return render(request, 'registration/login.html')


@login_required(redirect_field_name="login")
def userDetails(request, pk):
    user = UserModel.objects.get(id=pk)
    return render(request, 'registration/userDetails.html', {'staff': user})


@login_required(redirect_field_name="login")
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(redirect_field_name="login")
def deleteUser(request, pk):
    user = UserModel.objects.get(id=pk)
    user.delete()
    messages.success(request, 'User deleted successfully')
    return redirect('login')
