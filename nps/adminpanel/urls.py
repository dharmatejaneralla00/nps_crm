from django.urls import path
from . import views

urlpatterns = [
    path("", views.adminpanel, name='adminpanel'),
    path("dashboard", views.dashboard, name='dashboard'),
    path('editapplication/<str:uid>', views.Editapplication, name='editapplication'),
    path('editapplicationcopyright/<str:uid>', views.EditapplicationCopyright, name='editapplicationcopyright'),
    path('dashboard',views.dashboard),
    path('ndastatus',views.ndsatatus,name = 'ndastatus'),
    path('closeapplication',views.closeapplication,name = 'closeapplication'),
    path('openapplication',views.openapplication,name = 'openapplication'),
    path('FilingStatus',views.filingstatus,name = 'FilingStatus'),
    path('track',views.track,name='track')
]
