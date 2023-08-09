from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Patient
# Create your views here.

class PatientList(ListView):
    model=Patient
    context_object_name ='patient'
    template_name = 'list.html'


class PatientCreate(CreateView):
    model=Patient
    fields='__all__'
    success_url=reverse_lazy("patient")
    template_name = 'patientcreate.html'

class PatientUpdate(UpdateView):
    model=Patient
    fields='__all__'
    success_url=reverse_lazy("patient")
    template_name = 'patientcreate.html'

class PatientDelete(DeleteView):
    model=Patient
    fields='__all__'
    success_url=reverse_lazy("patient")
    template_name = 'patientdel.html'

class PatientDetail(DetailView):
    model=Patient
    template_name = 'patientdetail.html'

