from django import forms
from django.contrib.auth.models import User
from . models import Book,Account

from . import models
class BookForm(forms.ModelForm):

    class Meta:
        model=Book
        fields=['bk_title','bk_author','bk_cat','bk_publisher','bk_pubyear','bk_pubagency','bk_edition','bk_isbn','bk_noofpages','bk_price','bk_stno']
        labels={

            'bk_title':'Book Title',
            'bk_author':'Book Author',
            'bk_cat':'Book Category',
            'bk_publisher': 'Book Publisher',
            'bk_pubyear': 'Book Published Year',
            'bk_pubagency': 'Book Published Agency',
            'bk_edition': 'Book Edition',
            'bk_isbn': 'Book ISBN',
            'bk_noofpage': 'Book pages',
            'bk_price': 'Book Price',
            'bk_stno': 'Book Stock',

        }
widegts={
    'bk_title':forms.TextInput(attrs={'class':'form-control'}),
    'bk_author':forms.TextInput(attrs={'class':'form-control'}),
    'bk_publisehr':forms.TextInput(attrs={'class':'form-control'}),
    'bk_pubyear':forms.TextInput(attrs={'class':'form-control'}),
    'bk_pubagency':forms.TextInput(attrs={'class':'form-control'}),
    'bk_isbn':forms.TextInput(attrs={'class':'form-control'}),
    'bk_noofpages':forms.TextInput(attrs={'class':'form-control'}),
    'bk_price':forms.TextInput(attrs={'class':'form-control'}),
    'bk_stno':forms.TextInput(attrs={'class':'form-control'}),
}

class userupdateform(forms.ModelForm):
    # email= forms.EmailField()

    class Meta:
        model = Account
        fields = ['fname','lname','email','contact','address','city','state','pincode','dob']