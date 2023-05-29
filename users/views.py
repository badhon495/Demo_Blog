from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST': #user er pathano http request check kortese
        form = UserRegisterForm(request.POST)
        if form.is_valid():   #to check the password and username validity 
            form.save() #to save the user on database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!') #it will show a flash message.
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    
    if request.method == 'POST':  #what does this request.method eexactly mean?
        u_form = UserUpdateForm(request.POST,instance=request.user) #we used instance beacuse it will show the current username and email adderess on the form, which will make easier if customer want to change anything. request.POST means everything that customer submitted. not sure though
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)  #request.FILES to access the photo customer uploaded.
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)
