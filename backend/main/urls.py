from django.urls import path
from .import views

urlpatterns = [
    path('',views.landingPage, name='landingPage'),
    path('Orphans/',views.OrphanList.as_view(),name='OrphanList'),
    path('OrphanDetails/<int:pk>/',views.OrphanDetails.as_view(),name='OrphanDetails'),
    path('AddOrphan/',views.AddOrphan.as_view(),name='AddOrphan'),
]