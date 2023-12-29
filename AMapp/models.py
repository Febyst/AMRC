from django.db import models

class Contact(models.Model):
    c_name = models.CharField(max_length=250)
    c_email = models.EmailField()
    c_type = models.CharField(max_length=300)
    c_message = models.TextField()

    def _str_(self):
        return self.email

class customers(models.Model):
    c_fname = models.CharField(max_length=350)
    c_lname = models.CharField(max_length=350)
    c_addr = models.TextField()
    c_city = models.CharField(max_length=300)
    c_mail = models.EmailField()
    c_zip = models.IntegerField()
    c_state = models.CharField(max_length=200)
    c_phone = models.IntegerField()
    c_cindate = models.DateField()
    c_coutdate = models.DateField()
    c_driver = models.IntegerField()
    c_apt = models.CharField(max_length=200)
    c_vtype = models.CharField(max_length=300)
    c_vmod = models.CharField(max_length=250)
    c_trans = models.CharField(max_length=200)
    c_splints = models.TextField()