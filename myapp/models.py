from django.db import models
class UserAccount(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50,default='user')
    status=models.IntegerField(default=0,blank=True)
    class Meta:
        db_table="login"

class Investor(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address=models.CharField(max_length=50,blank=True)
    mobile=models.CharField(max_length=20)
    email=models.EmailField()
    country=models.CharField(max_length=50)
    investortype=models.CharField(max_length=50)
    status=models.IntegerField(default=0,blank=True)
    class Meta:
        db_table="investor" 

class Owner(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address=models.CharField(max_length=50,blank=True)
    mobile=models.CharField(max_length=20)
    email=models.EmailField()
    country=models.CharField(max_length=50)
    companyprofile=models.CharField(max_length=500)
    domain=models.CharField(max_length=50)
    status=models.IntegerField(default=0)
    class Meta:
        db_table="owner"

class Project(models.Model):
    projectid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    hours=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)
    status=models.IntegerField(default=1)
    class Meta:
        db_table="project"

class PResponse(models.Model):
    quotedby=models.CharField(max_length=50)
    projectid=models.IntegerField()
    quotedamount=models.IntegerField()
    quotedby=models.CharField(max_length=50)
    status=models.IntegerField()
    class Meta:
        db_table="presponse"

class ProjectResponse(models.Model):
    quotedby=models.CharField(max_length=50)
    quotedamount=models.IntegerField()
    projectid=models.IntegerField()   
    status=models.IntegerField()
    class Meta:
        db_table="projectresponse"

class Feedback(models.Model):
    username=models.CharField(max_length=50,default='')
    describe=models.CharField(max_length=500) 
    #status=models.IntegerField()
    class Meta:
        db_table="feedback"

        


