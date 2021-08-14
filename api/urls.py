from .views import UserListView, employeeDetailInterface, employeeDetailView, employeeListInterface, employeeListView
from django.urls import path

urlpatterns = [
    path('api/employee', employeeListView),
    path('api/employee/<int:pk>', employeeDetailView),
    path('api/employeeinter', employeeListInterface),
    path('api/employeeinter/<int:pk>', employeeDetailInterface),
    path('api/users', UserListView),
    
]
