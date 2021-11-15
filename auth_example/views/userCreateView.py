from rest_framework                         import status, views
from rest_framework.response                import Response
from rest_framework_simplejwt.serializers   import TokenObtainPairSerializer

from auth_example.serializers.userSerializer import UserSerializar

class UserCreateView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializar(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        token_data = {"username": request.data['username'],
                      "password": request.data['password']}

        token_serializar = TokenObtainPairSerializer(data = token_data)
        token_serializar.is_valid(raise_exception=True)
        return Response(token_serializar.validated_data, status=status.HTTP_201_CREATED)


