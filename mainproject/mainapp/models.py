from django.db import models

# Create your models here.


class Student(models.Model):
    fullname = models.CharField(max_length=100, null=True, db_index=True)
    email = models.CharField(max_length=100, null=True, db_index=True)
    password = models.CharField(max_length=100, null=True, db_index=True)



class Instructor(models.Model):
    fullname = models.CharField(max_length=100, null=True, db_index=True)
    email = models.CharField(max_length=100, null=True, db_index=True)
    password = models.CharField(max_length=100, null=True, db_index=True)

class Courses(models.Model):
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="course_instructor_id", null=True)
    course_name = models.CharField(max_length=100, null=True, db_index=True)
    course_type =  models.CharField(max_length=10, null=True, db_index=True)
    amount = models.CharField(max_length=10, null=True, db_index=True)
    course_file = models.FileField(upload_to="course_file", null=True, db_index=True)
    course_link = models.CharField(max_length=250, null=True, db_index=True)
    contact_number = models.CharField(max_length=50, null=True, db_index=True)


class StudentCourses(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_course_student_id",
                                      null=True)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="student_course_course_id",
                                      null=True)

