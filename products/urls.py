from django.urls import path
from . import views

app_name='products'
urlpatterns = [
    path('', views.index, name='menumain'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:product_id>/edit/', views.edit, name='edit'),
    path('<int:product_id>/update/', views.update, name='update'),
    path('<int:product_id>/delete/', views.delete, name='delete'),
    #path('<int:post_id>/like/', views.like, name='like'),
    ]