from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainer, Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# List trainers
def trainers_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'bookings/trainers_list.html', {'trainers': trainers})

# Book an appointment
@login_required
def book_appointment(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  # Assign current user to appointment
            appointment.trainer = trainer  # Assign the selected trainer
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('appointment_confirmation', appointment_id=appointment.id)
        else:
            # Re-render form with errors
            return render(request, 'bookings/book_appointment.html', {'form': form, 'trainer': trainer})
    else:
        form = AppointmentForm(initial={'trainer': trainer})

    return render(request, 'bookings/book_appointment.html', {'form': form, 'trainer': trainer})

# Appointment confirmation
def appointment_confirmation(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'bookings/appointment_confirmation.html', {'appointment': appointment})
