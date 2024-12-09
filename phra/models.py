# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CdPatient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=True, db_comment='first name or last name for ppl from other country.')
    last_name = models.CharField(max_length=30, blank=True, null=True, db_comment='first name or last name for ppl from other country.')
    patient_system_id = models.CharField(unique=True, max_length=100, db_comment='e.g. SAP ID')

    class Meta:
        managed = False
        db_table = 'cd_patient'


class LabRecord(models.Model):
    record_id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(CdPatient, on_delete=models.CASCADE)
    lab_record_id = models.CharField(unique=True, max_length=100)
    appointment_note = models.TextField(blank=True, null=True)
    result_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_record'


class LabResults(models.Model):
    result_id = models.BigAutoField(primary_key=True)
    spec_amount = models.CharField(max_length=100, blank=True, null=True)
    spec_description = models.CharField(max_length=50, blank=True, null=True)
    lab_record = models.ForeignKey(LabRecord, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'lab_results'
