from django.db import models

# Create your models here.

class Journalists(models.Model):
    name=models.CharField(max_length=250)
    surname=models.CharField(max_length=250)
    biography=models.TextField()


    def __str__(self):
        return f"{self.name} {self.surname}"

class Articles(models.Model):
    author=models.ForeignKey(Journalists,on_delete=models.CASCADE,related_name='articles')
    title=models.CharField(max_length=250)
    body=models.TextField()
    context=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    published_date=models.DateField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=False)



    def __str__(self):
        return self.title
