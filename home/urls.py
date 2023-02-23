from django.urls import path
from . import views
urlpatterns= [
    path('',views.home),
    path('about/',views.about),
    path('login/',views.login,name='login'),
    path('base/',views.base),
    path('reg/',views.reg,name='reg'),
    path('contact/',views.contact),
    path('services/',views.service),
    path('rules/',views.rules),
    path('user',views.user,name='user'),
    path('logout/',views.logout,name='logout'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('librarian/',views.librarian,name='librarian'),
    path('display',views.display,name='display'),
    path('bookdisplay',views.bookdisplay,name='bookdisplay'),
    path('add/',views.add,name='add'),
    path('<int:bk_id>',views.view,name='view'),
    path('edit/<int:bk_id>/', views.edit, name='edit'),
    path('delete/<int:bk_id>/', views.delete, name='delete'),
    path('profile/',views.profile,name='profile'),
    path('profile/update/',views.profile_update,name='profileupdate'),
    path('prof/',views.prof,name='prof'),
    path('prof1/', views.prof1, name='prof1'),
    path('profupdate/',views.prof_update,name='profupdate'),
    path('prof1update/',views.prof1_update,name='prof1update'),
    path('searchbar/',views.searchbar,name='searchbar'),
    path('search/', views.search, name='search'),
    path('requestbook/<int:bk_id>/',views.requestbook,name='requestbook'),
    path('approved/<int:id>/',views.approved,name='approved'),
    path('viewsrequest/',views.viewsrequest,name='viewsrequest'),
    path('issuebooklib/',views.issuebooklib,name='issuebooklib'),
    path('return_approve/<int:id>/',views.return_approve,name='return_approve'),
    path('returnbook/',views.returnbook,name='returnbook')
    # path('issuedbookuser', views.issuedbookuser, name='issuedbookuser'),


]



