"""talktome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#test
from django.views.generic import TemplateView
from django.conf.urls import url,include
from django.contrib import admin
from talktomee import settings
from django.conf.urls.static import static
#from talktome.users.api import urls
from django.conf.urls import url, include
from django.contrib.auth.models import User
from posts.models import Post
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'title', 'slug', 'content', 'updated', 'timestamp', 'publish' , 'draft' )


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)



urlpatterns = [ 
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^users/',include('users.urls')),
    url(r'^posts/', include("posts.urls", namespace='posts')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
