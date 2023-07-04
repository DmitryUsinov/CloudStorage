from Storage.views import *
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, MEDIA_URL, DEBUG


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('upload_file/', model_form_upload, name='upload_file'),
    path('add_discipline/',AddDiscipline.as_view(), name='add_discipline'),
    path('discipline/', DisciplineHome.as_view() , name='discipline'),
    path('discipline/<int:id>/', disc_detail, name='disc_detail_url'),
    path('delete-file/<str:slug>', deleteFile, name='delete_file'),
    path('delete-discipline/<int:id>', DisciplineHome.deleteDiscipline, name='delete_discipline'),

]
if DEBUG:
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)

