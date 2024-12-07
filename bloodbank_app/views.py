from django.contrib import messages, auth
from django.contrib.auth import login, update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from bloodbank_app.bbforms import bloodbank_reg
from bloodbank_app.forms import UserReg, Customer_reg, Need_blood
from bloodbank_app.models import bloodrequest, Customers, bloodbank


# Create your views here.
def homepage(request):
    return render(request,'index.html')
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('HomeAdmin')
        elif user is not None and user.is_customer:
            login(request,user)
            return redirect('HomeUser')
        elif user is not None and user.is_community:
            login(request, user)
            return redirect('HomeDonor')
        else:
            messages.info(request, 'Invalid username or password.')

    return render(request,'log.html')

def admin_page(request):
    return render(request,'bloodbank_admin.html')


def Cus_reg(request):
    form1=UserReg()
    form2=Customer_reg()
    if request.method=='POST':
        form1 = UserReg(request.POST)
        form2 = Customer_reg(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user=form1.save(commit=False)
            user.is_customer=True
            user.save()
            customer=form2.save(commit=False)
            customer.user=user
            customer.save()
            return redirect('loginpage')
            messages.info(request,'customer registered successfully')
    return render(request,'login.html',{'form1':form1,'form2':form2})

def bb_reg(request):
    form1 = UserReg()
    form2 = bloodbank_reg()
    if request.method == 'POST':
        form1 = UserReg(request.POST)
        form2 = bloodbank_reg(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_community = True
            user.save()
            bloodbank = form2.save(commit=False)
            bloodbank.user = user
            bloodbank.save()
            return redirect('loginpage')
            messages.info(request, 'bloodbank registered successfully')
    return render(request, 'bloodlog.html', {'form1': form1, 'form2': form2})
def userpage(request):
    current_name = request.user
    user_id = current_name.username
    print(user_id)
    context = {'user_id' : user_id}
    return render(request, 'userpage.html')

def bloodbankpage(request):
    return render(request, 'bloodbankpage.html')


def NeedBlood(request):
    u = request.user
    form = Need_blood()
    if request.method == 'POST':
        form = Need_blood(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            # Add a success message
            messages.success(request, "Request sent successfully!")
            return redirect('NeedBlood')  # Redirect to the same page to show the message
    return render(request, 'Need_Blood.html', {'form': form})

def RequestHistory(request):
    data=bloodrequest.objects.filter(user = request.user)
    return render(request,'Request_history.html',{'data':data})



def Uview_profile(request):
    user = request.user
    data = Customers.objects.filter(user=user)
    context = {'data': data}
    return render(request, 'Uview_profile.html',context)

def HomeUser(request):
    user = request.user
    data = Customers.objects.filter(user=user)
    context = {'data': data}
    return render(request,'homeuser.html',context)
def UD_status(request):
    user = request.user
    data = bloodrequest.objects.filter(user=user)
    return render(request, 'UD_status.html', {'data': data})

 # Redirect after success


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important: Keeps the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')  # Change to the appropriate success page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})




def Base(request):
    return render(request, 'base.html')



def user_logout(request):
    logout(request)
    return redirect('homepage')  # Redirect to user home page



