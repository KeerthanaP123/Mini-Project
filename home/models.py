from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from distutils.command.upload import upload
from django.contrib.auth.models import User
import datetime
from fileinput import  filename
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.contrib import messages



class MyAccountManager(BaseUserManager):
    def create_user(self, fname, lname, email, contact, address, city, state, pincode, dob,  is_customer, is_librarian,password=None):

        if not email:
            raise ValueError("user must have an email address")
        user=self.model(
           email=self.normalize_email(email),
           fname=fname,
           lname=lname,
           contact=contact,
           address=address,
           city=city,
           state=state,
           pincode=pincode,
           dob=dob,
           is_customer=is_customer,
           is_librarian=is_librarian,


        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self,password,email,**extra_fields):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password, **extra_fields

         )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user




# from django.contrib.auth.models import PermissionsMixin
class Account(AbstractBaseUser):
    status_choices=(('Approved','Approved'),('Pending','Pending'),('None','None'))
    role_choices=(('is_customer','is_customer'),('is_librarian','is_librarian'),('None','None'))
    id = models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50,default='')
    lname=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=100,unique=True)
    contact=models.BigIntegerField(default=0)
    address=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    state=models.CharField(max_length=50,default='')
    pincode=models.BigIntegerField(default='0')
    dob=models.DateField(default=0)

    aadharno=models.BigIntegerField(default=0)
    roles=models.CharField(max_length=100,choices=role_choices,default='')
    status=models.CharField(default='Pending',choices=status_choices,max_length=40)
    #required
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_librarian=models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname','contact','address','city','state','pincode','dob','is_customer','is_librarian','aadharno']

    #REQUIRED_FIELDS = ['username','password']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.fname} {self.lname}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True




class Category(models.Model):
    cat_name=models.CharField(max_length=200,unique=True)

    class Meta:
        ordering = ('cat_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format((self.cat_name))

class Book(models.Model):

    bk_id = models.AutoField(primary_key=True)
    bk_title = models.CharField(max_length=100)
    bk_author = models.CharField(max_length=100)
    bk_cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    bk_publisher = models.CharField(max_length=200)
    bk_pubyear = models.BigIntegerField()
    bk_pubagency = models.CharField(max_length=200)
    bk_edition = models.BigIntegerField()
    bk_isbn = models.BigIntegerField()
    bk_noofpages = models.BigIntegerField()
    bk_price = models.BigIntegerField()
    bk_stno=models.BigIntegerField()



    def __str__(self):
        return str(self.bk_title)+"["+str(self.bk_isbn)+']'

class Profile_update(models.Model):
    email=models.OneToOneField(Account, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username}-Profile'



class BookRequest(models.Model):
    requestdate=models.DateTimeField(auto_now_add=True)
    bookid=models.ForeignKey(Book,on_delete=models.CASCADE)
    userid=models.ForeignKey(Account,on_delete=models.CASCADE)
    requestedstatus=models.BooleanField(default=False)

class tbl_BookIssue(models.Model):
    issue_id=models.AutoField(primary_key=True)
    reqid=models.ForeignKey(BookRequest,on_delete=models.CASCADE)
    date_of_issue=models.DateTimeField(auto_now_add=True)
    issuedstatus=models.BooleanField(default=False)

class tbl_BookReturn(models.Model):
    return_id=models.AutoField(primary_key=True)
    issue_id=models.ForeignKey(tbl_BookIssue,on_delete=models.CASCADE)
    date_of_return=models.DateTimeField(auto_now_add=True)