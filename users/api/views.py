from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import list_route
from .serializers import UserSerializer
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from django.http import JsonResponse

#@authentication_classes((SessionAuthentication, BasicAuthentication))
#@permission_classes((IsAuthenticated,))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticated,)



@list_route(methods=['GET', 'DELETE', 'POST'])
def token(self, request, *args, **kwargs):
    """
    This view only returns the token of the currently logged in user

    GET returns the current token
    POST generates a new token
    DELETE removes the current token
    """
    if request.method in ('DELETE', 'POST'):
        Token.objects.filter(user=request.user).delete()
        if request.method == 'DELETE':
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            Token.objects.create(user=request.user)

        serializer = UserTokenSerializer(request.user)

        return Response(serializer.data)

def update(self, request, *args, **kwargs):
    if self.request.user != self.get_object():
        raise PermissionDenied

    return super(UserViewSet, self).update(request, args, kwargs)



    
    

