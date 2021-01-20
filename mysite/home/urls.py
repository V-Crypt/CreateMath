
from django.urls import include, path
from . import views
from django.views.generic import TemplateView

app_name="home"

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/',include('django.contrib.auth.urls'), name="accounts"),
    path("logout", views.log_user_out, name="logout"),
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
    # path('accounts/detalles/', views.student_details, name="detalles")
]