from django.db import models


# Create your models here.
# make migrations- see the changes in the modals
# migrate-apply all the changes in the models such as create the table
# after creating go to admin.py register the modals
# step 3 go to setting in installed app register the app name
class booking(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subject = models.TextField(default='')
    message = models.TextField()
    date = models.DateTimeField

    def __str__(self):
     return self.name

CHOICES=[('1','definetely'),
         ('2','maybe'),
         ('3','not Sure')]

rolech=[('1','individual',),
        ('2','couple'),('3','smallgroup'),('4','largegroup'),('5','preferno')]

pur=[('1','Date'),
         ('2','birthday'),
         ('3','anniversary'),
     ('4','party')]



class table(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    age= models.IntegerField()

    role=models.CharField( max_length=2,choices=rolech,default='')
    prefer= models.TextField(max_length=30,null=True,blank=True)
    purpose = models.CharField(max_length=2,choices=pur,default='')
    comment= models.TextField(max_length=300,null=True,blank=True)


    def __str__(self):
     return self.name

