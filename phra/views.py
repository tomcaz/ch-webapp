from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import CdPatient, LabRecord, LabResults


def index(request):
    return HttpResponse("")


def patient_list(request):
    patient_data = CdPatient.objects.order_by('last_name')
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
    try:
        cd_patient = CdPatient(patient_system_id=patient_id, first_name=first_name, last_name=last_name)
        cd_patient.save()
    except IntegrityError:
        context = {
            'error_message' : "Patient Serial Number is already exists",
            'patient_id': patient_id
        }
        return render(request, "phra/patient-form.html", context)
    return HttpResponse("Patient Added. Click <a href='/'>here</a> to view.")


def records_list(request, patient_id):
    patient = get_object_or_404(CdPatient, pk=patient_id)
    records = LabRecord.objects.filter(patient_id=patient_id)
    context = {
        "records": records,
        "patient": patient
    }
    return render(request, "phra/record-list.html", context)


def records_form(request, patient_id):
    context = {
        'patient_id': patient_id
    }
    return render(request, "phra/record-form.html", context)


def records_add_submit(request, patient_id):
    lab_result = request.POST['labResult']
    lab_record_id = request.POST['labRecordId']
    prescription = request.POST['prescription']
    appointment_note = request.POST['appointmentNote']
    try:
        lab_record = LabRecord(patient_id=patient_id, lab_record_id=lab_record_id, appointment_note=appointment_note)
        lab_record.save()

        record_id = lab_record.record_id
        for result in lab_result.split(','):
            save_lab_result(lab_record, result, 1)
        for result in prescription.split(','):
            save_lab_result(lab_record, result, 2)
    except:
        context = {
            'error_message' : 'Unable to save record',
            'patient_id': patient_id
        }
        return render(request, "phra/record-form.html", context)
    return HttpResponse(
        f"Lab Record Added. Click <a href='/records/{patient_id}'>here</a> to view.")

def save_lab_result(lab_record, data, type):
    if "-" in data:
        d = data.split("-")
        lab_result = LabResults(lab_record=lab_record,spec_amount= d[0], spec_description=d[1], type = 1)
        lab_result.save()
    else :
        lab_result = LabResults(lab_record=lab_record,spec_amount= data, spec_description='', type = 2)
        lab_result.save()


def record_detail(request, record_id):
    lab_record = get_object_or_404(LabRecord,pk=record_id)
    patient = get_object_or_404(CdPatient,pk=lab_record.patient.patient_id)
    lab_results = LabResults.objects.filter(lab_record = lab_record)
    context = {
        'lab_record': lab_record,
        'patient': patient,
        'lab_results': filter(lambda result : result.type == 1, lab_results),
        'prescriptions': filter(lambda result : result.type == 2, lab_results)
    }
    return render(request, "phra/record-detail.html", context)