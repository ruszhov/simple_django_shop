from django.contrib import admin
from .models import *
# Register your models here.

class ProductImageInline(admin.TabularInline):		#ств клас ProductImageInline щоб добавити його в адмінці до розділу продукти(тобто коли зайдем на конкретний продукт, то в низ убудуть і фотки з моделі ProductImage)
	model = ProductImage			
	extra = 0


class ProductCategoryAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductCategory._meta.fields]

	class Meta:
		model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Product._meta.fields]
	inlines = [ProductImageInline]					#Прописуєми атрибут який відобразить фотки ProductImageInline в розділі з продуктом
	
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductImage._meta.fields]
	
	class Meta:
		model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)