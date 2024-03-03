from django.db import models

class Course(models.Model):
    autor = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    date = models.DateField(verbose_name='start date', auto_now=False)
    min_quantity = models.PositiveSmallIntegerField()
    max_quantity = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.title
    
class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.URLField(verbose_name='link', null=False)

    def __str__(self):
        return self.title
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def full_name(self):
        full_name = str(self.first_name + ' ' + self.last_name)
        return full_name

    def __str__(self):
        return self.full_name()
    
class Group(models.Model):
    g_course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    members = models.ManyToManyField(Student, through='Membership')

    def __str__(self):
        return self.title
    
class Membership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.student.full_name()
        

    

        


# Create your models here.
