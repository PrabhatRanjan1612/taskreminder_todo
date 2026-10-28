from django.urls import path
from . import views

urlpatterns = [
    path('',views.intro,name="homepage"),
    path('Login/',views.login, name="login_user"),
    path("Register/", views.register, name="register_user"),
    path("Forgetpass/" , views.forget , name="forget_pass"),
    path("addTask/" , views.addtask , name="addtask"),
    path("alltask/",views.alltask , name="alltask"),
    path("logout/",views.log_out , name="logout"),
    path("<int:task_id>", views.Task_update , name="taskupdate"),
    path("/<int:task_id>" , views.Task_trash , name="tasktrash"),
    path("details/<int:task_id>" , views.details_task , name="task_details"),
    path("about/", views.aboutApp , name="aboutApp"),
    path("/updateTask/<int:task_id>" , views.updateTaskDetails , name="updateTask")
]
