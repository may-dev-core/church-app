from django.db import models

# Create your models here.
GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
)

class Member(models.Model):
    member_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER)
    phone_number_1 = models.CharField(max_length=100, null=True, blank=True)
    phone_number_2 = models.CharField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


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
