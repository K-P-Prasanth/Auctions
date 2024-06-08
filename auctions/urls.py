from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create",views.create,name="create"),
    path("view/<int:item_id>",views.view,name="view"),
    path("watch",views.watch,name="watch"),
    path("deleteitem",views.deleteitem,name="deleteitem"),
    path("delete",views.delete,name="delete"),
    path("cat",views.cat,name="cat")
]
