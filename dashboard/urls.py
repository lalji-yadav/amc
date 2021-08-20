from django.urls import path, include
from . import views


urlpatterns = [
    path('table/', views.data),
    path('table2/', views.data2),
    path('', views.dashboard),
    path('addAmc', views.addAmc),
    path('paidAmc/', views.paidAmc),
    path('pendingAmc/', views.pendingAmc),
]
