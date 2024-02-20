from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Case(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gpa = models.FloatField()
    sat_act = models.FloatField()
    ielts = models.FloatField(blank=True, null=True)
    toefl = models.FloatField(blank=True, null=True)
    essay = models.FileField(verbose_name='case_essay',
                             upload_to='case_essay/',
                             blank=True, null=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user}, {self.first_name}, {self.last_name}'


class Achievements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="achievements_case")
    case = models.ForeignKey(Case, on_delete=models.CASCADE,
                             related_name="achievements_case")
    title = models.CharField(max_length=60)
    description = models.TextField()
    file = models.FileField(upload_to="achievements_case/",
                            null=True, blank=True,
                            verbose_name="Achievements_Case")
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user}, {self.case}, {self.case.first_name}'


class EducationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='educ_history')
    case = models.ForeignKey(Case, on_delete=models.CASCADE,
                             related_name='educ_history')
    school = models.CharField(max_length=200)
    description = models.TextField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=60, blank=True)
    file = models.FileField(upload_to="educ_history/",
                            null=True, blank=True,
                            verbose_name="Education_History")

    def __str__(self):
        return f'{self.user}, {self.case}, {self.case.first_name}'

