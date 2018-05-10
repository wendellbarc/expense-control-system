from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BankAccount(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    agency = models.CharField(max_length=6, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    when_opened = models.DateField()

    @property
    def balance(self):
        today = timezone.now()
        result = 0
        current_date = self.when_opened
        while current_date <= today:
            result -= sum(x.total for x in self.cashing.on_date(current_date))
            result += sum(x.total for x in self.deposits.on_date(current_date))
            current_date += timedelta(days=1)
        return result


class OperationManager(models.Manager):

    def on_date(self, date):
        return (super(OperationManager, self).get_queryset()).filter(when__gte=date, when__lte=date)



class Deposit(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='deposits')
    total = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    when = models.DateTimeField()

    objects = OperationManager()

class Cashing(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='cashing')
    total = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    when = models.DateTimeField()

    objects = OperationManager()
