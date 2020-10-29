from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class activity(models.Model):
	name_5 = models.CharField(max_length=50,default="",null=False)
	day = models.IntegerField(default = 0,null=False)
	oneline_5 = models.CharField(max_length=500,default="",null=False)
	description_5 = RichTextField(default=1)
	image_1_5 = models.ImageField(upload_to='activity_images',default="",null=True,blank=True)
	image_2_5 = models.ImageField(upload_to='activity_images',default="",null=True,blank=True)
	video_5 = models.CharField(max_length=500,default="")
	unique_one_word_name_5 = models.CharField(max_length=10,default="",null=False)

	name_8 = models.CharField(max_length=50,default="",null=False)
	oneline_8 = models.CharField(max_length=500,default="",null=False)
	description_8 =RichTextField(default=1)
	image_1_8 = models.ImageField(upload_to='activity_images',default="",null=True,blank=True)
	image_2_8 = models.ImageField(upload_to='activity_images',default="",null=True,blank=True)
	video_8 = models.FileField(upload_to='videos',default="",null=True,blank=True)
	unique_one_word_name_8 = models.CharField(max_length=10,default="",null=False)

	def __str__(self):
			return self.name_5



