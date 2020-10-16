from django.urls import path
from . import views

# Created variable app_name
app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),

# Added path for displays list of all blogs
    path('<int:blog_id>/', views.detail, name='detail'),


]
