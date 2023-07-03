from django.db import models

# Create your models here.
class bankModel(models.Model):
    accountno=models.IntegerField(max_length=50)
    name=models.CharField(max_length=20)
    balance=models.IntegerField(max_length=200)
    



    def __str__(self):
        return "accountno={0},name={1},balance={2}".format(self.accountno,self.name,self.balance)


class bankdetail(models.Model):
    date=models.DateField()
    time=models.TimeField()
    