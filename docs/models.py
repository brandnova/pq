from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Faculty(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Semester(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='items')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='items')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='items')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='items')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='items')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='PQ_images', blank=True, null=True)
    file = models.FileField(upload_to='PQ_files', blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

