from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('upload/', views.upload_note, name='upload'),
    path('notes/', views.note_list, name='note_list'),
    path('download/<int:note_id>/', views.download_note, name='download'),
    # Add your course URLs here
    # path('', views.course_list, name='course_list'),
]
