from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('app',views.app,name='app'),
    path('report',views.report,name='report'),
    path('reports',views.reportsAll,name='reports'),
    path('reports/<r_id>',views.reports,name='reports'),
]