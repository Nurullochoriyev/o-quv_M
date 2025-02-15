from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=55)
    tel_nomer=models.CharField(max_length=13)
    email=models.EmailField(unique=True)
    created_ad=models.DateTimeField(auto_now_add=True)
    updated_ad=models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Student"
        verbose_name_plural="Student"
        ordering=['pk']



class Curs(models.Model):
    title=models.CharField(max_length=200)
    start_time=models.TimeField()
    end_time=models.TimeField()
    descripions=models.TextField()
    created_ad=models.DateTimeField(auto_now_add=True)
    updated_ad=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Curs"
        verbose_name_plural="Curs"
        ordering=['pk']
