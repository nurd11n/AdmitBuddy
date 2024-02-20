from django.db import models

# Create your models here.


class Universities(models.Model):
    naming = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()


class UniversitiesImage(models.Model):
    image = models.FileField(upload_to="universities_image/")
    universities = models.ForeignKey(Universities, on_delete=models.CASCADE, related_name="images")


class UniversitiesFaculty(models.Model):
    universities = models.ForeignKey(Universities, on_delete=models.CASCADE, related_name="universities_faculty")
    faculty_naming = models.CharField(max_length=50)
    description = models.TextField()
    teacher = models.CharField(max_length=50)
    price = models.PositiveIntegerField()


class UniversitiesFacultyImage(models.Model):
    universities_faculty = models.ForeignKey(UniversitiesFaculty, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="universities_faculty_image/")
