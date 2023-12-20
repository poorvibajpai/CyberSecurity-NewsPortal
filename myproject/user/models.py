from django.db import models


# Create your models here.


class category(models.Model):
    cname = models.CharField(max_length=30)
    cpic = models.ImageField(upload_to='static/category/', default="")
    cdate = models.DateField()

    def __str__(self):
        return self.cname


class news(models.Model):
    city = models.CharField(max_length=200)
    headlines = models.CharField(max_length=500)
    subject = models.CharField(max_length=800)
    newsdetail = models.TextField(max_length=8000)
    newspic = models.ImageField(upload_to='static/news/', default="")
    ndate = models.DateField()
    ncategory = models.ForeignKey(category, on_delete=models.CASCADE)


class notification(models.Model):
    ndes = models.TextField(max_length=5000)
    ndate = models.DateField()


class video(models.Model):
    vtitle = models.CharField(max_length=200)
    vdes = models.TextField(max_length=600)
    thumb = models.ImageField(upload_to='static/thumbnail/', default="")
    vlink = models.CharField(max_length=500)
    vdate = models.DateField()


class slider(models.Model):
    stitle = models.CharField(max_length=200)
    sdes = models.CharField(max_length=500)
    spic = models.ImageField(upload_to='static/slider/', default="")
    sdate = models.DateField()


class SignUp(models.Model):
    Firstname = models.CharField(max_length=25)
    LastName = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Dob = models.DateField()
    Password = models.CharField(max_length=30)
    ConfirmPassword = models.CharField(max_length=30)
 
    def __str__(self):
        return self.Firstname


class Login(models.Model):
    Email = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    confirmPassword = models.CharField(max_length=30)

    def __str__(self):
        return self.Email
