from django.db import models #доступ к коду из других файлов
from django.utils import timezone

class Post(models.Model): #модель по имени Post
	autor = models.ForeignKey('auth.User') #автор - ссылка на другую модель
	title = models.CharField(max_length=200) #название - текстовое поле с ограничением на кол-во символов
	text = models.TextField() #текст - текстовое поле с неограниченным кол-вом символов
	created_date = models.DateTimeField(
		default=timezone.now) #дата создания - дата и время
	published_date = models.DateTimeField(
		blank=True, null=True) #дата публикации - дата и время

	def publish(self): #метод публикации, где def - означает создание метода, publish - имя метода.
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title