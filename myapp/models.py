from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=29, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        manage = false
        db_table = 'form'

class Ownership(models.Model):
    house_no = models.IntegerField(blank=True, null=True)
    ward_no = models.IntegerField(blank=True, null=True)
    tole = models.CharField(max_length=100, blank=True, null=True)
    house_owner = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'ownership'


class Residence(models.Model):
    residence = models.BigIntegerField(primary_key = True)
    ownership_type = models.CharField(max_length=100)
    house_type = models.CharField(max_length=100, blank=True, null=True)
    land_type = models.CharField(max_length=100, blank=True, null=True)
    total_room = models.CharField(max_length=101, blank=True, null=True)
    house_use = models.CharField(max_length=101, blank=True, null=True)
    house_area = models.CharField(max_length=101, blank=True, null=True)
    earthquake_resistance = models.CharField(max_length=101, blank=True, null=True)
    id = models.ForeignKey(Ownership, models.DO_NOTHING, db_column='id')

    class Meta:
        db_table = 'residence'


class ServiceDetail(models.Model):
    service = models.BigIntegerField(primary_key=True)
    radio = models.BooleanField(blank=True, null=True)
    television = models.BooleanField(blank=True, null=True)
    telephone = models.BooleanField(blank=True, null=True)
    computer = models.BooleanField(blank=True, null=True)
    internet = models.BooleanField(blank=True, null=True)
    motorcycle = models.BooleanField(blank=True, null=True)
    car = models.BooleanField(blank=True, null=True)
    refrigerator = models.BooleanField(blank=True, null=True)
    washing_machine = models.BooleanField(blank=True, null=True)
    heater = models.BooleanField(blank=True, null=True)
    id = models.ForeignKey(Ownership, models.DO_NOTHING, db_column='id')

    class Meta:
        db_table = 'service_detail'