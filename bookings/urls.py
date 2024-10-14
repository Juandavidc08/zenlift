from django.urls import path
from . import views

urlpatterns = [
    path('trainers/', views.trainers_list, name='trainers_list'),
    path('book/<int:trainer_id>/', views.book_appointment, name='book_appointment'),
    path('confirmation/<int:appointment_id>/', views.appointment_confirmation, name='appointment_confirmation'),
]
