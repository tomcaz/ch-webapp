from django.http import HttpResponse
from django.shortcuts import render
from .models import CdPatient, LabRecord


def index(request):
    return HttpResponse("")


def patient_list(request):
    patient_data= CdPatient.objects.order_by('last_name')
    context = {
        "patient_data": patient_data
    }
    print(patient_data)
    return render(request, "phra/patient-list.html", context)


def patient_form(request):
    return render(request, "phra/patient-form.html")


def patient_add_submit(request):
    first_name = request.POST['firstName']
    last_name = request.POST['lastName']
    patient_id = request.POST['patientId']
    cd_patient = CdPatient(patient_system_id=patient_id, first_name=first_name, last_name=last_name)
    cd_patient.save()
    return HttpResponse("Patient Added. Click <a href='/patients'>here</a> to view.")


def records_list(request, patient_id):
    # patient_data= LabRecord.objects.order_by('last_name')
    # context = {
    #     "patient_data": patient_data
    # }
    # print(patient_data)
    # return render(request, "phra/record-list.html", context)
    return HttpResponse(patient_id)