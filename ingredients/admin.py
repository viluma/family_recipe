from django.contrib import admin

# Register your models here.

from .models import Category, Ingredients, Recipe, Part, Steps, Unit, Author





class StepsInLine(admin.TabularInline):
   model = Steps
   



class PartInLine(admin.TabularInline):
   model = Part
   



class IngredientsInLine(admin.TabularInline):
   model = Ingredients
   





class AdminPart(admin.ModelAdmin):
	inlines=[IngredientsInLine, StepsInLine]










class AdminRecipe(admin.ModelAdmin):
	inlines=[PartInLine ]
	
	












admin.site.register(Recipe, AdminRecipe)

admin.site.register(Part, AdminPart)
admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Author)


