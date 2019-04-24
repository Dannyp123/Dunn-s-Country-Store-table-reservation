from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class TableReservation(models.Model):
    f_name = models.TextField()
    l_name = models.TextField()
    phone_regex = RegexValidator(
        regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')
    p_number = models.CharField(validators=[phone_regex], max_length=10)
    num_of_people = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    email = models.EmailField()

    @staticmethod
    def submit_reservation(f_name, l_name, p_number, num_of_people, date, time,
                           email):
        TableReservation(
            f_name=f_name,
            l_name=l_name,
            p_number=p_number,
            num_of_people=num_of_people,
            date=date,
            time=time,
            email=email).save()
