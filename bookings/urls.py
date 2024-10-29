from django.urls import path
from . import views
from .views import update_appointment, delete_appointment

urlpatterns = [
    path('', views.trainers_list, name='trainers_list'),
    path('book/<int:trainer_id>/', views.book_appointment, name='book_appointment'),
    path('confirmation/<int:appointment_id>/', views.appointment_confirmation, name='appointment_confirmation'),
     # Payment-related URL patterns
    path('payment/<int:appointment_id>/', views.payment, name='payment'), 
    path('payment_success/<int:appointment_id>/', views.payment_success, name='payment_success'),  
    path('payment_cancel/', views.payment_cancel, name='payment_cancel'),
    path('appointment/update/<int:appointment_id>/', update_appointment, name='update_appointment'),
    path('appointment/delete/<int:appointment_id>/', delete_appointment, name='delete_appointment'),  
]