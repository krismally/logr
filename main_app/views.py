from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Log


# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # creates a user form object
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # adds user to database
            user = form.save()
            # logs in user
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # either bad POST or a GET request, render signup.html with empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def logs_index(request):
    logs = Log.objects.filter(user=request.user)
    return render(request, 'logs/index.html', {'logs': logs})