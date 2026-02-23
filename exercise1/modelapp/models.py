from django.db import models 

class Book(models.Model):
    name = models.CharField(max_length= 10)
    rate = models.IntegerField(default= 0)
    free = models.BooleanField(default= True)
    author = models.ForeignKey("Profile", on_delete= models.CASCADE, related_name='books')
    

    def __str__(self):
        return f"{self.name} {self.id} {self.rate}"
    
class User(models.Model):
    email = models.EmailField()
    is_active = models.BooleanField()
    is_admin = models.BooleanField()
    
    def __str__(self):
        return self.email
    
    
class Profile(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    mobile = models.IntegerField()
    user_id = models.OneToOneField(User, on_delete= models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name}"
    
class Library(models.Model):
    code = models.PositiveIntegerField()
    title = models.CharField(max_length= 100)
    user_id = models.ForeignKey(Profile, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title