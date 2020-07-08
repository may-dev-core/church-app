from django.db import models
from datetime import date
from decimal import *
# Create your models here.
GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
)

TEMPS_TENS = (
    (0, 0),
    (30, 3),
)

TEMPS_ONES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
)

TEMPS_DECIMALS = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
)


SERVICE = (
    ('1', '1st Service'),
    ('2', '2nd Service'),
    ('Joint', 'Joint Service'),
)


class Member(models.Model):
    member_id = models.AutoField(
        unique=True, help_text='Auto generated, do not change!', primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER)
    location = models.CharField(
        max_length=255, null=True, blank=True, help_text='Town/Residence/House number')
    phone_number_1 = models.CharField(max_length=100, null=True, blank=True)
    phone_number_2 = models.CharField(max_length=100, null=True, blank=True)
    visitor = models.BooleanField(
        default=False, help_text='For only visitors')

    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.middle_name is None:
            self.middle_name = " "
        return f'{str(self.member_id)} - {self.first_name} {self.middle_name} {self.last_name}'

    def get_member_id(self):
        return self.member_id

    # def save(self, *args, **kwargs):
    #     try:
    #         self.member_id = int(Member.objects.order_by(
    #             'member_id').last().member_id) + 1
    #     except Exception as e:
    #         self.member_id = 1001

    #         print(f'Error {e}')
    #     super(Member, self).save(*args, **kwargs)


class Attendance(models.Model):
    date = models.DateField(default=date.today)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    present = models.BooleanField(default=True)
    child = models.BooleanField(
        default=False, help_text='For only children')
    temp_tens = models.IntegerField(choices=TEMPS_TENS, default=0)
    temp_ones = models.IntegerField(choices=TEMPS_ONES, default=0)
    temp_decimals = models.IntegerField(choices=TEMPS_DECIMALS, default=0)
    temperature = models.FloatField(null=True, blank=True)
    service = models.CharField(max_length=100, choices=SERVICE, default='1')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.member)

    # def save(self, *args, **kwargs):
    #     try:
    #         sum_tens_ones = self.temp_tens + self.temp_ones
    #         str_temp = str(sum_tens_ones) + "." + str(self.temp_decimals)
    #         self.temperature = float(str_temp)
    #     except Exception as e:
    #         self.temperature = 37.0

    #         print(f'Error {e}')
    #     super(Attendance, self).save(*args, **kwargs)


# class MemberProfile(models.Model):
#     member = models.CharField(max_length=20, unique=True)
#     first_name = models.CharField(max_length=100)
#     middle_name = models.CharField(max_length=100, null=True, blank=True)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField(null=True, blank=True)
#     gender = models.CharField(max_length=6, choices=GENDER)
#     location = models.CharField(max_length=255, null=True, blank=True)
#     phone_number_1 = models.CharField(max_length=100, null=True, blank=True)
#     phone_number_2 = models.CharField(max_length=100, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.first_name + " " + self.last_name)
