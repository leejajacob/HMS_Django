from django.urls import path

from .views import PatientList, PatientCreate, PatientUpdate, PatientDelete, PatientDetail

urlpatterns=[
    path('list/', PatientList.as_view(), name='patient'),
    path('create/', PatientCreate.as_view(), name='patient-create'),
    path('update/<int:pk>', PatientUpdate.as_view(), name='patient-update'),
    path('delete/<int:pk>', PatientDelete.as_view(), name='patient-delete'),
    path('details/<int:pk>', PatientDetail.as_view(), name='patient-detail'),

]