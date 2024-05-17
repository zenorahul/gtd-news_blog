from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Editor(models.Model):
    editor_id =  models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    editor_name = models.CharField(max_length=20)
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Publisher(models.Model):
    publisher_id =models.CharField(primary_key=True)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    Publisher_name =models.CharField(max_length=40)

class Journal(models.Model):
    journal_id = models.CharField(primary_key=True)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    journal_name = models.CharField(max_length=20)
    designation = models.CharField(max_length=100)
    about =models.TextField()
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    Editor_id =models.ForeignKey(Editor,on_delete=models.CASCADE)
    publisher_id =models.ForeignKey(Publisher,on_delete=models.CASCADE)

class Article(models.Model):
    ARTICLE_ID =models.IntegerField(primary_key = True,default=True)
    HEADING= models.CharField(max_length=100,null=True)
    CONTENT =models.TextField(blank=True,null=True)
    GENRE= models.CharField(max_length=20,null=True)
    SUB_GENRE =models.CharField(max_length=20,null=True)
    PREMIUM =models.BooleanField(blank=True,null=True)
    VIDEO_URL =models.CharField(max_length=50,null=True)
    AUDIO_BLOB =models.BinaryField(null=True)
    JOURNAL_ID= models.ForeignKey(Journal, on_delete=models.CASCADE,null=True)
    STATUS =models.CharField(max_length=3,null=True)
    PUBLISH_TIME =models.DateField(blank=True,null=True)

class ArticleImg(models.Model):
    IMG_ID=models.IntegerField(primary_key = True,default=True)
    ARTICLE_ID= models.ForeignKey(Article, on_delete=models.CASCADE)
    IMG_BLOB =models.BinaryField(null=True)

class User(models.Model):
    USER_ID=models.IntegerField(primary_key = True,default=True)
    NAME= models.CharField(max_length=100,null=True)
    USERNAME= models.CharField(max_length=20,unique=True)
    PASSWORD= models.CharField(max_length=20)
    def save(self, *args, **kwargs):
        if self.PASSWORD:
            self.PASSWORD = make_password(self.PASSWORD)
        super().save(*args, **kwargs)

    MAIL_ID= models.CharField(max_length=50,null=True)
    AC_TYPE= models.CharField(max_length=20,null=True)
    SUB_START= models.DateField(blank=True,null=True)
    SUB_END= models.DateField(blank=True,null=True)