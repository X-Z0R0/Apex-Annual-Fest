from django.urls import path
from .views import *

urlpatterns = [
    path('<int:u_id>/',Technoagaaz_Page, name='Technoagaaz'),  #from landpage
    path('registration_Technoagaaz/<int:u_id>/',Technoagaaz_Registrations,name='registration_Technoagaaz'),  #from _Spoorti
    path('info/<str:game>/<int:u_id>',info,name='TeamInfo'),                                     #from register
    path('TechnoagaazDashboard/',dashboard,name='TechnoagaazDashboard'),              
    path('delete_team/<id>/',delete_team,name="Delete_Technoagaaz_Team"),
]
