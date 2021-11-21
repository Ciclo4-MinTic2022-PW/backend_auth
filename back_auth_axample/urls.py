from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from auth_example                   import views

urlpatterns = [
    
    path('admin/',          admin.site.urls),
    path('login/',          TokenObtainPairView.as_view()),
    path('refresh/',        TokenRefreshView.as_view()),
    path('verifyToken/',           views.VerifyTokenView.as_view()),
    path('user/',           views.UserCreateView.as_view()),
    path('user/<int:pk>',   views.UserDetailView.as_view()),
    path('userdelete/<int:pk>',   views.UserDeleteView.as_view()),
    path('userupdate/<int:pk>',   views.UserUpdateView.as_view()),


]
