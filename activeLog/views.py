from django.shortcuts import render
from django.contrib import messages
from django.contrib import auth
from .models import Profile, activity_periods
from django.contrib.auth.models import User
import datetime
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password) 
        if user is not None:
            auth.login(request, user)
            return render(request,'index.html')
        else:   
            messages.error(request, 'Error wrong username/password') 
    return render(request, 'login.html')  
def logout(request):
    auth.logout(request)
    return render(request,'logout.html')
from .forms import SignUpForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.timezone = form.cleaned_data.get('timezone')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return render(request,'index.html')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def home(request):
    return render(request,'index.html')
from django.http import JsonResponse

#This api for genrating the json
def gen_jason(request):
    users = User.objects.all()
    data = {"ok":True,"members":[]}
    for user in users:
        profile = Profile.objects.get(user = user)
        ap = activity_periods.objects.filter(profile = profile)
        pdata = {}
        if ap:
            pdata["id"] = str(user.id)
            pdata["real_name"] = ((user.first_name if user.first_name else "admin") +" " + user.last_name).strip()
            pdata["tz"]= profile.timezone
            pdata["activity_periods"]=[]
            for i in ap: 
                dat ={"start_time":i.start_time.strftime("%b %d %Y %I:%M%p"),"end_time":i.end_time.strftime("%b %d %Y %I:%M%p")}
                pdata["activity_periods"].append(dat)
            data["members"].append(pdata)
    return  JsonResponse(data,json_dumps_params={'indent': 4})