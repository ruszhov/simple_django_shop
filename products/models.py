from django.db import models

class ProductCategory(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return '%s' % self.name 	#по замовчуванню виводитись буде ім'я

	class Meta:
		verbose_name = 'Категорія товару'
		verbose_name_plural = 'Категорії товарів'


class Product(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	discount = models.IntegerField(default=0)	#знижка
	category = models.ForeignKey(ProductCategory, blank=True, null=True, default=0)
	short_description = models.TextField(blank=True, null=True, default=None)
	description = models.TextField(blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)	
	created = models.DateTimeField(auto_now_add=True, auto_now=False)	#поле створюється автоматично при ств запису в Produkct
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)	#значення буде змінено коли робиться любий update

	def __str__(self):
		return '%s %s' % (self.price, self.name)

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товари'


class ProductImage(models.Model):
	session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
	product = models.ForeignKey(Product, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='products_images/')
	is_main = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)	#поле створюється автоматично при ств запису в Product
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)	#значення буде змінено коли робиться любий update

	def __str__(self):
		return '%s' % self.id

	class Meta:
		verbose_name = 'Фотографія'
		verbose_name_plural = 'Фотографії'
