from django.urls import path
from django.contrib.auth import views as auth_views
from bloodbank_app import views, adminviews, donorviews

urlpatterns=[path('',views.homepage,name="homepage"),
             path('loginpage',views.loginpage,name="loginpage"),
             path('admin_page',views.admin_page,name="admin_page"),
             path('Cus_reg',views.Cus_reg,name="Cus_reg"),
             path('bb_reg',views.bb_reg,name="bb_reg"),
             path('userpage',views.userpage,name="userpage"),
             path('bloodbankpage', views.bloodbankpage, name="bloodbankpage"),
             path('viewCustomer',adminviews.viewCustomer,name="viewCustomer"),
             path('viewBloodbank',adminviews.viewBloodbank,name="viewBloodbank"),
             path('deleteCustomer/<int:id>/',adminviews.deleteCustomer,name="deleteCustomer"),
             path('deleteBloodbank/<int:id>/',adminviews.deleteBloodbank,name="deleteBloodbank"),
             path('NeedBlood',views.NeedBlood,name="NeedBlood"),
             path('Bloodrequest',adminviews.Bloodrequest,name="Bloodrequest"),
             path('Approvalrequest/<int:id>/',adminviews.Approvalrequest,name="Approvalrequest"),
             path('Rejectrequest/<int:id>/',adminviews.Rejectrequest,name="Rejectrequest"),
             path('RequestHistory',views.RequestHistory,name="RequestHistory"),
             path('View_request',donorviews.View_request,name="View_request"),
             path('Dview_profile',donorviews.Dview_profile,name="Dview_profile"),
             path('Idonate/<int:id>/',donorviews.Idonate,name="Idonate"),
             path('Donorrequest',adminviews.Donorrequest,name="Donorrequest"),
             path('Uview_profile',views.Uview_profile,name="Uview_profile"),
             path('RequestHistory', views.RequestHistory, name="RequestHistory"),
             path('HomeAdmin',adminviews.HomeAdmin,name="HomeAdmin"),
             path('BloodStock',adminviews.BloodStock,name="BloodStock"),
             path('HomeDonor',donorviews.HomeDonor,name="HomeDonor"),
             path('UD_status',views.UD_status,name="UD_status"),
             path('Donor_History',donorviews.Donor_History,name="Donor_History"),
             path('change_password/', views.change_password, name='change_password'),
             path('donor_changepassword/', donorviews.donor_changepassword, name='donor_changepassword'),
             path('HomeUser', views.HomeUser, name='HomeUser'),
             path('Base', views.Base, name='Base'),
             path('donor_id_card/<int:user_id>/', adminviews.donor_id_card_view, name='donor_id_card_view'),
             path('id_card/<int:user_id>/', adminviews.id_card_view, name='id_card_view'),
             path('admin_logout/', adminviews.admin_logout, name='admin_logout'),
             path('user_logout/', views.user_logout, name='user_logout'),
             path('donor_logout/', donorviews.donor_logout, name='donor_logout')



             ]