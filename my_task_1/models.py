
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.exceptions import ValidationError

def username_validator(value):
    
    if len(value) < 2:
        raise ValidationError("User Name Should have atleast 2 Characters")
    else:
        if value[0] not in ['a', 'A']:
            raise ValidationError("User Name Should start with 'A' or 'a'")
        if value[-1] not in ['1', '0']:
            raise ValidationError("User Name Should end with '1' or '0'")

def title_validator(value):
    if len(value) < 10:
        raise ValidationError("Task Title Should be of atleast 10 Characters")

class UserManager(BaseUserManager):
    def create_user(self, username="", password=""):
        if username == "":
            raise ValidationError("Please Enter valid username")
        if password == "":
            raise ValidationError("Please Enter valid password")
        user = self.model(
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username="", password=""):
        user = self.create_user(username = username)
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    uid = models.AutoField
    username = models.CharField(max_length=10, unique=True, validators=[username_validator])
    join_date = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=1000)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    objects = UserManager()
    def __str__(self):
        return self.username
    
    def has_module_perms(self,app_label):
        return True
    def has_perm(self,perm,obj=None):
        return self.is_staff

class Task(models.Model):
    tid = models.AutoField
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=20, validators=[title_validator])
    task_description = models.CharField(max_length=2000, blank=True, null=True)
    task_pic = models.ImageField(upload_to="Images/", default="null")
    create_time_stamp = models.DateTimeField(auto_now_add=True)

  