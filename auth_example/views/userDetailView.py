from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework                         import status, generics
from rest_framework.response                import Response
from rest_framework.permissions             import IsAuthenticated
from rest_framework_simplejwt.backends      import TokenBackend 

from auth_example.models.user               import User
from auth_example.serializers               import UserSerializar

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializar

    def get (self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializar

    def put (self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializar

    def delete (self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class UserDeleteViewReserva(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializar
    permission_clasess = (IsAuthenticated, )

    def delete (self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm= settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify= False)

        if valid_data['user_id'] != kwargs['pk']:
            string_response = {'Detail': 'Acceso no autorizado.'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)

        

