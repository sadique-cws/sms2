
from django.contrib import admin
from django.urls import path
from school.views import homepage, deleteStudent
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage),
    path("/delete/<int:id>/", deleteStudent, name="delete"),
]