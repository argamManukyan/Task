from django.db import models
from django.contrib.auth.models import User

USER_GROUPS = [
    ('F', 'Физическое лицо'),
    ('U', 'Юридическое лицо'),
]


class Terms(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Qualification(models.Model):
    icon = models.FileField(upload_to='qualification_icons')
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', editable=False, null=True, blank=True)
    terms = models.ManyToManyField(Terms,related_name='terms')
    qualification = models.ForeignKey(Qualification,on_delete=models.SET_NULL,null=True,blank=True)
    group = models.CharField(choices=USER_GROUPS, max_length=20,null=True)
    name = models.CharField(max_length=50,null=True)
    middle_name = models.CharField(max_length=50,null=True)
    surname = models.CharField(max_length=50,null=True)
    serial_number = models.CharField(max_length=50,null=True)
    brd_date = models.DateField(null=True)
    dep_code = models.CharField(max_length=20,null=True)
    issued_by = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=20,null=True)
    front_image = models.FileField(upload_to='passport_image',null=True)
    back_image = models.FileField(upload_to='passport_image',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_qualified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"



