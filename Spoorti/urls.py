from django.urls import path
from .views import *

urlpatterns = [
    path('/',spoorti_page, name='Spoorti'),  #from landpage
    # path('registration_spoorti/<int:u_id>/',spoorti_registrations,name='registration_spoorti'),  #from _Spoorti
    path('info/<str:game>/<int:u_id>',info,name='teamInfo'),                                     #from register
    path('SpoortiDashboard/',dashboard,name='SpoortiDashboard'),    
     path('Status/',PaymentStatus,name='PaymentStatus'),          
    path('delete_team/<id>/',delete_team,name="Delete_Spoorti_Team"),
]
