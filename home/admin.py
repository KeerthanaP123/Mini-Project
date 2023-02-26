from django.contrib import admin
from django.contrib.auth.models import Group
from . models import Category,Account,Book,elibrary
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse
import csv
# #  Register your models here.
admin.site.unregister(Group)
admin.site.site_header="Library"
admin.site.site_title="Welcome To Admin's Dashboard"
admin.site.index_title="Welcome to public Library"


class AccountAdmin(UserAdmin):
    list_display = ('fname','lname','email','contact','address','city','state','pincode','roles','status')
    ordering=('fname',)
    search_fields = ('fname','email')
    filter_horizontal = ()
    list_per_page = 50
    list_filter = ('fname','email')
    filedsets=()
    list_display_links = ('email')


admin.site.register(Book)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['cat_name']
    search_fields = ('cat_name',)
class elibraryy(admin.ModelAdmin):
    list_display = ['title','book_author','book_pdf']
    ordering = ('title',)
    search_fields = ('title', 'book_author',)
    filter_horizontal = ()
    list_per_page = 50
admin.site.register(elibrary)

class bookdisplay(admin.ModelAdmin):
    list_display = ['bk_title']
    search_fields = ['bk_title','bk_author','bk_cat']
    ordering = ('bk_title',)
    filter_horizontal = ()
    list_per_page = 50
    list_filter = ('bk_title', 'bk_author')
    filedsets = ()
    list_display_links = ('bk_title')
admin.site.register(Category,Categoryadmin)
def export_reg(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registration.csv"'
    writer = csv.writer(response)
    writer.writerow(['First Name','Last Name','Email','Contact','Address','City','State','Pincode','Role'])
    registration = queryset.values_list('fname','lname','email','contact','address','city','state','pincode','role')
    for i in registration:
        writer.writerow(i)
    return response


export_reg.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','contact','address','city','state','pincode','dob']
    actions = [export_reg]
admin.site.register(Account,RegAdmin)

