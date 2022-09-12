from django.urls import path

from . import views
urlpatterns = [
    path('login', view=views.UserLogIn.as_view(), name="LogIn"),
    path('signup', view=views.UserSignUp.as_view(), name="SignUp"),
    path('home_page', view=views.homeView.as_view(), name="HomePage"),
    path('first_screen', view=views.FirstScreenView.as_view(), name="First"),
    path('second_screen', view=views.SecondScreenView.as_view(), name="Second"),
    path('third_screen', view=views.ThirdScreenView.as_view(), name="Third"),
    path('output_first', view=views.selectimagefirst.as_view(), name="Output"),
    path('output_second', view=views.selectimagesecind.as_view(), name="Output"),
    path('output_third', view=views.selectimagethird.as_view(), name="Output") ,
]
