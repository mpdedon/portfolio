from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    technology = models.CharField(max_length=30)
    github_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])

    def __str__(self) -> str:
        return self.title