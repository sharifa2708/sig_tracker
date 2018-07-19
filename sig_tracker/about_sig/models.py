from django.db import models

# Create your models here.
class Sig(models.Model):
<<<<<<< HEAD
     sig_name = models.CharField(blank= False, max_length=100)
     co_ordinator = models.CharField(max_length=250)
     sig_logo = models.CharField(max_length= 1000)
     about = models.TextField(blank= True)
     created = models.DateTimeField(auto_now_add= True)
     modified = models.DateTimeField(auto_now= True)

     def __str__(self):
         return self.sig_name

class Topics(models.Model):
    sig_name = models.ForeignKey(Sig, on_delete = models.CASCADE)
    topic_name = models.CharField(max_length = 1000)
=======
    sig_name = models.CharField(blank=False, max_length=100)
    co_ordinator = models.CharField(max_length=250)
    sig_logo = models.CharField(max_length= 1000)
    about = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return self.sig_name

class Topics(models.Model):
    sig_name = models.ForeignKey(Sig, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=1000)
>>>>>>> upstream/master
    co_ordinator = models.CharField(max_length=250)
    conductors = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    topic_gist = models.TextField(blank=True)
    resources = models.TextField(blank=True)
<<<<<<< HEAD

    def  __str__(self):
        return self.topic_name




=======
    
    def  __str__(self):
        return self.topic_name
>>>>>>> upstream/master
