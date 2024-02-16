from django.urls import path
from .views import register_user, user_login, user_logout, create_content, list_content, content_detail, search_content, \
    admin_view_all_content, admin_edit_delete_content

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('content/create/', create_content, name='create_content'),
    path('content/list/', list_content, name='list_content'),
    path('content/detail/<int:pk>/', content_detail, name='content_detail'),
    path('content/search/', search_content, name='search_content'),

    path('admin/content/all/', admin_view_all_content, name='admin_view_all_content'),
    path('admin/content/edit/<int:pk>/', admin_edit_delete_content, name='admin_edit_delete_content'),
]