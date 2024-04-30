from datetime import datetime

from django.db import models


# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    usertype = models.CharField(max_length=200)


class subadmin(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)


class volunteer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    Login = models.ForeignKey(login, default=1, on_delete=models.CASCADE)
    SUBADMIN = models.ForeignKey(subadmin, default=3, on_delete=models.CASCADE)


class precaution(models.Model):
    description = models.CharField(max_length=200)
    file = models.CharField(max_length=200)


class donation(models.Model):
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)


class adminmessage(models.Model):
    message = models.CharField(max_length=200)
    mdate = models.CharField(max_length=200,default=datetime.now().date())

class camp(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    SUBADMIN = models.ForeignKey(subadmin, default=1, on_delete=models.CASCADE)


class campallocation(models.Model):
    CAMP = models.ForeignKey(camp, default=1, on_delete=models.CASCADE)
    Volunteer = models.ForeignKey(volunteer, default=1, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)


class whether(models.Model):
    city = models.CharField(max_length=200,default=1)
    weather = models.CharField(max_length=200,default=1)
    date = models.CharField(max_length=200,default=datetime.now().now())
    temp = models.CharField(max_length=200,default=1)
    description = models.CharField(max_length=200,default=1)
    humidity = models.CharField(max_length=200,default=1)
    pressure = models.CharField(max_length=200,default=1)


class alert(models.Model):
    alert = models.CharField(max_length=200)
    alert_date = models.CharField(max_length=20,default=1)
    latitude = models.CharField(max_length=20,default=1)
    longitude = models.CharField(max_length=20,default=1)


class bank(models.Model):
    name = models.CharField(max_length=200)
    accno = models.CharField(max_length=200)
    ifsc = models.CharField(max_length=200)
    balance = models.CharField(max_length=200)


class subemergency(models.Model):
    message = models.CharField(max_length=200)
    SUBADMIN = models.ForeignKey(subadmin, default=1, on_delete=models.CASCADE)
    date = models.CharField(max_length=200, default=datetime.now().now())


class complaintesandreply(models.Model):
    complaints = models.CharField(max_length=200)
    reply = models.CharField(max_length=200,default='pending')
    complaintdate = models.CharField(max_length=200, default=datetime.now().date())
    replydate = models.CharField(max_length=200, default=1)
    VOLUNTEER = models.ForeignKey(volunteer, default=1, on_delete=models.CASCADE)



class feedback(models.Model):
    feedback = models.CharField(max_length=200)
    feedbackdate = models.CharField(max_length=200,default=datetime.now().date())
    VOLUNTEER = models.ForeignKey(volunteer, default=1, on_delete=models.CASCADE)



class SLOT(models.Model):
    totalslot = models.CharField(max_length=200)
    currentslot = models.CharField(max_length=200)
    VOLUNTEER = models.ForeignKey(volunteer, default=1, on_delete=models.CASCADE)


class needs(models.Model):
    list = models.CharField(max_length=200)
    quantityt = models.CharField(max_length=200)
    date = models.CharField(max_length=200, default=datetime.now().date())
    status =  models.CharField(max_length=200,default='pending')
    VOLUNTEER = models.ForeignKey(volunteer, default=1, on_delete=models.CASCADE)


class userdb(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    housename = models.CharField(max_length=200,default=1)
    place = models.CharField(max_length=200,default=1)
    post = models.CharField(max_length=200,default=1)
    pin = models.CharField(max_length=200,default=1)
    phno = models.CharField(max_length=200,default=1)
    joiningdate = models.CharField(max_length=200)
    dismisaldate = models.CharField(max_length=200)
    VOLUNTEER = models.ForeignKey(volunteer, default=1, on_delete=models.CASCADE)

