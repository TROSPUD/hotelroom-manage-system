# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    id = models.IntegerField(primary_key=True)
    account = models.TextField()
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255, blank=True, null=True)
    id_card = models.CharField(db_column='ID_card', max_length=255)  # Field name made lowercase.
    phone_number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customer'


class Order(models.Model):
    state = models.CharField(max_length=255)
    room = models.ForeignKey('Room', models.DO_NOTHING)
    cust = models.ForeignKey(Customer, models.DO_NOTHING)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    start_time = models.DateField()
    end_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'room'


class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    account = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'
