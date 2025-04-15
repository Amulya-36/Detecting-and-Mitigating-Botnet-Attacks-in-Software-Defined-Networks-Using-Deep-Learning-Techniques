from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=30)


class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class prediction_botnet_attack(models.Model):

    Fid= models.CharField(max_length=300)
    stime= models.CharField(max_length=300)
    flgs_number= models.CharField(max_length=300)
    proto= models.CharField(max_length=300)
    proto_number= models.CharField(max_length=300)
    saddr= models.CharField(max_length=300)
    sport= models.CharField(max_length=300)
    daddr= models.CharField(max_length=300)
    dport= models.CharField(max_length=300)
    pkts= models.CharField(max_length=300)
    bytes1= models.CharField(max_length=300)
    state= models.CharField(max_length=300)
    state_number= models.CharField(max_length=300)
    ltime= models.CharField(max_length=300)
    seq= models.CharField(max_length=300)
    duration= models.CharField(max_length=300)
    spkts= models.CharField(max_length=300)
    dpkts= models.CharField(max_length=300)
    sbytes= models.CharField(max_length=300)
    dbytes= models.CharField(max_length=300)
    rate= models.CharField(max_length=300)
    srate= models.CharField(max_length=300)
    drate= models.CharField(max_length=300)
    webcategory= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)
