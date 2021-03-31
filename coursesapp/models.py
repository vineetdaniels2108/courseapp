from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validators(self,postData):
        errors ={}
        
        if len(postData['name'])<5:
            errors['name'] = "Name should be more than 5 characters"
            
        if len(postData['desc'])<15:
            errors['description'] = "description should be more than 15 characters"
            
        return errors
    

class Course(models.Model):
    name = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects  = CourseManager()
    
    def __unicode__(self):
        return self.name
    
class Description(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.description
    
class Comments(models.Model):
    course = models.ForeignKey(Course, related_name='comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
