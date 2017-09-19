from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import auth,views



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = "index.html"), name = 'index'),
    url(r'^login/', auth.login, name = 'login'),
    url(r'^logout/', auth.logout, name = 'logout'),
    url(r'^register/', auth.register, name = 'register'),
    url(r'^user/(?P<user>[0-9a-zA-Z+.]+)', views.profile, name = 'profile'),
    url(r'^user/$', views.lists, name = 'user'),
    url(r'accounts/login', auth.login, name ="login"),
    
    ] 