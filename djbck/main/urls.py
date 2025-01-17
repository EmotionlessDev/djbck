from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get1/", views.get1, name="get1"),
    path("get2/", views.get2, name="get2"),
    path("get3/<int:number>/", views.get3, name="get3"),
    path("form/", views.render_form, name="form"),
    path("post1/", views.post1, name="post1"),
    path("postAndGet1/", views.postAndGet1, name="postAndGet1"),
    path("postAndGet2/<str:username>/", views.postAndGet2, name="postAndGet2"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path("user/<str:username>/", views.user_detail, name="user_detail"),
    path("user/<str:username>/edit/", views.edit_user, name="edit_user"),
    path("user/<str:username>/delete/", views.delete_user, name="delete_user"),
    path("users/", views.users_list, name="users_list"),

]
