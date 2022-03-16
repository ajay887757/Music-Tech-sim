from django.contrib import admin
from django.urls import path
from song.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginForm,name='login'),
    path('home/',f1,name="Ajay"),
    path('ajay/',f2,name="piyush"),
    path('pg3/',f3,name="amit"),
    path('Detail/<int:s_id>/',Detail,name="Detail"),
    path('Arthmetic/',operations,name="operations"),
    path('Add_students/',Add_student,name="Add_student"),
    path('Delete_student/<int:sid>/',Delete_student,name="delete"),
    path('Add_college/',Add_college,name='Add_college'),
    path('delete_college/<int:sid>/',delete_college,name='delete_college'),
    path('edit_students/<int:sid>/',edit_student,name="edit_student"),
    path('edit_college/<int:sid>/',edit_college,name="edit_college"),
    path('Logout/',Logout,name="Logout"),
    path('signup/',signup,name="signup"),
   # path('Add_univercity/',Add_college),\
    path('forget/',forget,name="forget")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
