from django.db import models

# Create your models here.


class MyappStudent(models.Model):
    user_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    mail_id = models.CharField(max_length=40)
    address = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)

    class Meta:
        db_table = 'myapp_student'

   