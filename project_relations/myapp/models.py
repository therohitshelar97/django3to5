from django.db import models

# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.sname

class Projects(models.Model):
    ptitle = models.CharField(max_length=255, null=True)
    pdescription = models.CharField(max_length=255, null=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE) 

    def __str__(self):
        return self.ptitle

class Person(models.Model):
    pname = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.pname

class Car_Collection(models.Model):
    cname = models.CharField(max_length=255, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cname} owned by {self.person} "

class Students(models.Model):
    sname = models.CharField(max_length=100, null=True)
    sage = models.IntegerField(null=True)

    def __str__(self):
        return self.sname

class Books(models.Model):
    bname = models.CharField(max_length=100, null=True)
    bauthor = models.CharField(max_length=100, null=True)
    students = models.ManyToManyField(Students)

    def __str__(self):
        return self.bname