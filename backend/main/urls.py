from django.urls import path
from .import views

urlpatterns = [
    path('login-orphanage/',views.CustomLoginView.as_view(),name='login-orphanage'),
    path('logout-orphanage/',views.logoutOrphanage,name='logout-orphanage'),
    path('register-orphanage/',views.RegisterPage.as_view(),name='register-orphanage'),
    path('',views.landingPage, name='landingPage'),
    path('Orphans/',views.OrphanList.as_view(),name='OrphanList'),
    path('OrphanDetails/<int:pk>/',views.OrphanDetails.as_view(),name='OrphanDetails'),
    path('AddOrphan/',views.AddOrphan.as_view(),name='AddOrphan'),
    path('Update-orphan-details/<int:pk>/',views.UpdateOrphanDetails.as_view(),name='UpdateOrphanDetails'),
    path('Remove-orphan/<int:pk>/',views.RemoveOrphan.as_view(),name='RemoveOrphan'),
    path('Adopt-me/',views.AdoptMe.as_view(),name='AdoptMe'),
    path('Donate/',views.Donate,name='Donate'),
    path('SuccessPage/',views.SuccessPage,name='SuccessPage'),
]