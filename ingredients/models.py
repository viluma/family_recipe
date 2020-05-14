from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.



User = get_user_model()



class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_picture = models.ImageField()

	def __str__(self):
		return self.user.username



class Category(models.Model):
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.title

		


class Recipe(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	categories = models.ManyToManyField(Category)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	thumbnail = models.ImageField()
	preparation_time = models.DurationField()
	cooking_time = models.DurationField()
	portions = models.IntegerField() 

	def __str__(self):
		return self.title




class Part(models.Model):
	recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.TextField()
	position = models.IntegerField() 

	def __str__(self):
		return self.name



class Steps(models.Model):
	part_id = models.ForeignKey(Part, on_delete=models.CASCADE)
	instructions = models.TextField()
	 

	def __str__(self):
		return self.instructions






class Unit(models.Model):
	name = models.CharField(max_length=100)
	 

	def __str__(self):
		return self.name






class Ingredients(models.Model):
	name = models.CharField(max_length=100)
	part_id = models.ForeignKey(Part, on_delete=models.CASCADE)
	unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE)
	amount = models.IntegerField() 

	def __str__(self):
		return self.name






	  