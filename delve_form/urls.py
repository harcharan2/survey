from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.survey_form, name='survey_insert' ),
    path('<int:id>/', views.survey_form, name='survey_update'),
    path('delete/<int:id>/', views.survey_delete, name='survey_delete'),
    path('list/', views.survey_list, name='survey_list')
]
