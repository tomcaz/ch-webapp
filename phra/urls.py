from django.urls import path

from . import views

app_name = "phra"
urlpatterns = [
    path("", views.index, name="index"),
    path("patients", views.patient_list, name="phra"),
    path("patients/add", views.patient_form, name="patient_form"),
    path("patients/add_submit", views.patient_add_submit, name="patient_add_submit"),
    path("records/<int:patient_id>", views.records_list, name="records"),
]
