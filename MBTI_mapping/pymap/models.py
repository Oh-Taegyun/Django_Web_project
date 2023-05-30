from django.db import models
# Create your models here.

class MappingPoint_E(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class MappingPoint_I(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class ContactForm_E(models.Model):
    MBTI_CHOICES = [
        ('E', 'E'),
        ('I', 'I'),
    ]
    
    INFLUENCE_CHOICES = [
        ('yes', '예'),
        ('no', '아니요'),
    ]
    
    mbti = models.CharField(max_length=1, choices=MBTI_CHOICES)
    influence = models.CharField(max_length=3, choices=INFLUENCE_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f"ContactForm #{self.id}"
    
class ContactForm_I(models.Model):
    MBTI_CHOICES = [
        ('E', 'E'),
        ('I', 'I'),
    ]
    
    INFLUENCE_CHOICES = [
        ('yes', '예'),
        ('no', '아니요'),
    ]
    
    mbti = models.CharField(max_length=1, choices=MBTI_CHOICES)
    influence = models.CharField(max_length=3, choices=INFLUENCE_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f"ContactForm #{self.id}"