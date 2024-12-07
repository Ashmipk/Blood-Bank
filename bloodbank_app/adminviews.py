from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from bloodbank_app.forms import UserReg, Customer_reg, Need_blood
from bloodbank_app.models import Customers, bloodbank, bloodrequest


def viewCustomer(request):
    data=Customers.objects.all()
    return render(request,'view_customer.html',{'data':data})
def viewBloodbank(request):
    data=bloodbank.objects.all()
    return render(request,'view_bloodbank.html',{'data':data})

def deleteCustomer(request,id):
    data=Customers.objects.get(user_id=id)
    data.delete()
    return redirect('viewCustomer')

def deleteBloodbank(request,id):
    data=bloodbank.objects.get(user_id=id)
    data.delete()
    return redirect('viewBloodbank')

def Bloodrequest(request):
    data=bloodrequest.objects.all()
    return render(request,'blood_request.html',{'data':data})


def HomeAdmin(request):
    total_customers = Customers.objects.count()
    total_donors = bloodbank.objects.count()
    total_bloodrequest = bloodrequest.objects.count()
    total_donorsrequest = bloodrequest.objects.filter(Approval_status = 3).count()
    total_AP = bloodbank.objects.filter(BloodType='A+').count()
    total_BP = bloodbank.objects.filter(BloodType='B+').count()
    total_ABP = bloodbank.objects.filter(BloodType='AB+').count()
    total_OP = bloodbank.objects.filter(BloodType='O+').count()
    total_AN = bloodbank.objects.filter(BloodType='A-').count()
    total_BN = bloodbank.objects.filter(BloodType='B-').count()
    total_ABN = bloodbank.objects.filter(BloodType='AB-').count()
    total_ON = bloodbank.objects.filter(BloodType='O-').count()


    print(total_customers, total_donors,total_bloodrequest,total_donorsrequest,total_AP+total_BP+total_ABP+total_OP+ total_AN+total_BN+total_ABN+total_ON,"*********************************************")
    context = {'total_customers': total_customers,
               'total_donors': total_donors,
               'total_bloodrequest': total_bloodrequest,
               'total_donorsrequest': total_donorsrequest,
               'total_bloodstock': total_AP+total_BP+total_ABP+total_OP+ total_AN+total_BN+total_ABN+total_ON
               }
    return render(request, 'homeadmin.html',context)

def BloodStock(request):
    total_AP = bloodbank.objects.filter(BloodType = 'A+').count()
    total_BP = bloodbank.objects.filter(BloodType='B+').count()
    total_ABP = bloodbank.objects.filter(BloodType='AB+').count()
    total_OP = bloodbank.objects.filter(BloodType='O+').count()
    total_AN = bloodbank.objects.filter(BloodType='A-').count()
    total_BN = bloodbank.objects.filter(BloodType='B-').count()
    total_ABN = bloodbank.objects.filter(BloodType='AB-').count()
    total_ON = bloodbank.objects.filter(BloodType='O-').count()
    print(total_AP,total_BP,total_ABP,total_OP,total_AN,total_BN,total_ABN,total_ON,"*****")
    context = {'total_AP': total_AP,
               'total_BP' : total_BP,
               'total_ABP': total_ABP,
               'total_OP': total_OP,
               'total_AN': total_AN,
               'total_BN': total_BN,
               'total_ABN': total_ABN,
               'total_ON': total_ON

    }
    return render(request,'bloodstock.html',context)


def Approvalrequest(request,id):
    blood = bloodrequest.objects.get(user_id=id)
    blood.Approval_status = 1
    blood.save()
    return redirect("Bloodrequest")

def Rejectrequest(request,id):
    blood = bloodrequest.objects.get(user_id=id)
    blood.Approval_status = 2
    blood.save()
    return redirect("Bloodrequest")

def Donorrequest(request):
    data=bloodrequest.objects.filter(Approval_status = 3)
    return render(request,'Idonate.html',{'data':data})


def id_card_view(request, user_id):
    customer = get_object_or_404(Customers, user_id=user_id)

    if customer.Id_card:
        with open(customer.Id_card.path, 'rb') as pdf_file:

            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="id_card.pdf"'
            return response
    else:
        return HttpResponse("No ID card available.")


def donor_id_card_view(request, user_id):
    # Retrieve the donor record using the user_id
    donor_record = get_object_or_404(bloodbank, user_id=user_id)

    # Check if the donor has an ID card
    if donor_record.Id_card:
        # Create an HTTP response to serve the file as a viewable PDF
        response = HttpResponse(donor_record.Id_card, content_type='application/pdf')

        # Set the Content-Disposition to inline to display the PDF in the browser
        response['Content-Disposition'] = f'inline; filename="{donor_record.Id_card.name}"'

        return response
    else:
        # If no ID card is found, return a message indicating this
        return HttpResponse("No ID card available for this donor.")


def admin_logout(request):
    logout(request)
    return redirect('homepage')


