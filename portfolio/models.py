from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_url = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    
    def __str__(self):
        return self.title