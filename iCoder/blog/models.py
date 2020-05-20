from django.db import models


# Create your models here.
class Aut(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Aut,on_delete=models.CASCADE)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    sno = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='blog/images')
    name = models.ForeignKey(Aut,on_delete=models.CASCADE)
    # email = models.CharField(max_length=100)

    Description = models.TextField()

    facebook_link = models.CharField(max_length=10000)
    linkedin_link = models.CharField(max_length=10000)
    twitter_link = models.CharField(max_length=10000)

    def __str__(self):
        return 'Author Name '