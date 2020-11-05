from django.conf.urls import url
from .import views

urlpatterns = [
url(r'$^', views.home, name='home'),
url('login',views.login, name='login'),
url('register',views.register,name='register'),
url('logout',views.logout,name='logout'),
url('attribute',views.attribute,name='attribute'),
url('results',views.results,name='results'),

]





