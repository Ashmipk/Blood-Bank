from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from bloodbank_app.models import bloodrequest, bloodbank


def View_request(request):
    data = bloodrequest.objects.filter(Approval_status = 1)
    return render(request,'view_request.html',{'data':data})


def Dview_profile(request):
    user = request.user  # Assuming user is authenticated
    data = bloodbank.objects.filter(user=user)  # Filter by logged-in user
    context = {'data': data}
    return render(request, 'Dview_profile.html', context)

def HomeDonor(request):
    total_bloodrequest = bloodrequest.objects.filter(Approval_status = 1).count()
    print(total_bloodrequest,"********")
    context = {'total_bloodrequest': total_bloodrequest,}
    return render(request,'homedonor.html',context)



def Idonate(request, id):
    u = request.user
    blood_request = get_object_or_404(bloodrequest, user_id=id)
    blood_bank = get_object_or_404(bloodbank, user=u)
    blood_request.Donar_Name = blood_bank.Name
    blood_request. Donar_Age = blood_bank.Age
    blood_request. Donar_BloodType = blood_bank.BloodType
    blood_request.Donar_Location = blood_bank.District + ", " + blood_bank.City
    blood_request. Donar_Number = blood_bank.Phone_No
    blood_request.Approval_status = 3
    blood_request.save()
    return redirect('View_request')

def Donor_History(request):
    current_donor = bloodbank.objects.get(user=request.user)
    data = bloodrequest.objects.filter(Donar_Name=current_donor.Name, Approval_status=3)
    return render(request, 'Donor_history.html', {'data': data})




def donor_changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important: Keeps the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('donor_changepassword')  # Change to the appropriate success page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'admin_password_chang.html', {'form': form})


def donor_logout(request):
    logout(request)
    return redirect('homepage')
