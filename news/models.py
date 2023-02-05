from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=250,blank=False,verbose_name='Заголовок')
    content=models.TextField(blank=True,verbose_name='Содержание')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Дата редактирования')
    photo= models.ImageField(upload_to='uploads/%Y/%m/%d/',verbose_name='Фотография',blank=True)
    is_published=models.BooleanField(default=False,verbose_name='Опубликовано')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = '1. НОВОСТИ'
        ordering = ['id']


class subCategory(models.Model):
    subCategoryID=models.BigAutoField(primary_key=True,verbose_name='ID')
    subCategoryTitle = models.CharField(max_length=250, db_index=True, verbose_name='Наименование элемента')
    subCategoryLink = models.TextField(verbose_name='Наименование элемента')

    def __str__(self):
        return self.subCategoryTitle

    class Meta:
        verbose_name = 'Элемент категории'
        verbose_name_plural = 'Справочник элементов '
        ordering = ['subCategoryID']

class category(models.Model):
    categoryID = models.BigAutoField(primary_key=True, verbose_name='ID')
    categoryTitle = models.CharField(max_length=250, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.categoryTitle

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Справочник категорий'
        ordering = ['categoryID']


class profilesIndex(models.Model):
    profileIndex_PK = models.BigAutoField(primary_key=True, verbose_name='ID')
    profileIndexTitle = models.CharField(max_length=250, db_index=True, verbose_name='Наименование Профиля')

    def __str__(self):
        return self.profileIndexTitle

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Справочник профилей'
        ordering = ['profileIndex_PK']

class profiles(models.Model):
    profileID = models.BigAutoField(primary_key=True, verbose_name='ID')
    profileIndex_FK = models.ForeignKey('profilesIndex',db_column='profileIndex_FK',to_field='profileIndex_PK', on_delete=models.PROTECT,verbose_name='Профиль')
    categoryID_FK = models.ForeignKey('category',db_column='categoryID_FK',to_field='categoryID', on_delete=models.PROTECT,verbose_name='Категория')
    subCategoryID_FK = models.ForeignKey('subCategory',db_column='subCategoryID_FK', on_delete=models.PROTECT,verbose_name='Элемент категории')


    class Meta:
        unique_together = ('profileIndex_FK', 'categoryID_FK', 'subCategoryID_FK')
        verbose_name = 'Профиль'
        verbose_name_plural = '2. ПРОФИЛИ'
        ordering = ['profileID']


class userRights(models.Model):
    rightID = models.BigAutoField(primary_key=True, verbose_name='ID')
    userID = models.ForeignKey(User,db_column='userID',to_field='id', on_delete=models.CASCADE,verbose_name='Пользователь')
    profilesIndex_FK = models.ForeignKey('profilesIndex',db_column='profilesIndex_FK',to_field='profileIndex_PK', on_delete=models.PROTECT,verbose_name='Прикрепленный профиль')


    class Meta:
        unique_together = ('userID', 'profilesIndex_FK')
        verbose_name = 'Права'
        verbose_name_plural = '3. ПРАВА ПОЛЬЗОВАТЕЛЕЙ'
        ordering = ['userID']
