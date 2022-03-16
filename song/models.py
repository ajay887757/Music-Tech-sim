from django.db import models
class univercity(models.Model):
    Name=models.CharField(max_length=100)
    contact=models.IntegerField()
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.Name

class college(models.Model):
    uni=models.ForeignKey(univercity,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=50)
    contact=models.IntegerField()
    Address=models.CharField(max_length=50)

    def __str__(self):
        return self.Name
class students(models.Model):
    clg=models.ForeignKey(college,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=30)
    Enrollment=models.CharField(max_length=15)
    Gmail=models.CharField(max_length=30)
    Number=models.IntegerField()
    image=models.FileField(null=True)

    def __str__(self):
        return self.Name
class friend(models.Model):
    Name=models.CharField(max_length=20)
    contact = models.IntegerField()
    DOB=models.CharField(max_length=10)

