from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='TaskListView'),
    path('cbvdetails/<int:pk>/', views.TaskDetailView.as_view(), name='TaskDetailView'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='TaskDeleteView')

]
