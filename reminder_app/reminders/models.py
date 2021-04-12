from django.db import models
from django.contrib.auth.models import User


class Subjects(models.Model):
    subject = models.CharField(max_length=200)


RECUR_DAYS = (
    ('2 days', '2 days'),
    ('3 days', '3 days'),
    ('4 days', '4 days'),
    ('5 days', '5 days'),
    ('6 days', '6 days'),
    ('7 days', '7 days'),
)

SUBJECTS = (
    ('Appointment', 'Appointment'),
    ('Meeting', 'Meeting'),
    ('Shopping', 'Shopping'),
    ('Personal', 'Personal'),
    ('Party', 'Party'),
    ('Other', 'Other'),
)


class Reminders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField('Title', max_length=100)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    date_of_reminder = models.DateField()
    subject = models.CharField('Subject', choices=SUBJECTS, max_length=100)
    description = models.TextField()
    email = models.EmailField('Email Id', blank=True, null=True)
    contact_no = models.PositiveIntegerField('Contact No.', blank=True, null=True)
    sms_no = models.PositiveIntegerField('SMS No.', blank=True, null=True)
    enabled = models.BooleanField('Enable', default=True)
    recur_for = models.CharField('Recur for', max_length=20, choices=RECUR_DAYS, blank=True, null=True)
