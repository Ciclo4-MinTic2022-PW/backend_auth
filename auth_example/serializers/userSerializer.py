from django.db.models               import fields
from rest_framework                 import serializers
from auth_example.models.user       import User


class UserSerializar(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'name',
            'email',
            'age',
            'location',
            'description'
        ]



    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id'            : user.id,
            'username'      : user.username,
            'name'          : user.name,
            'email'         : user.email,    
            'age'           : user.age,
            'location'      : user.location,
            'description'   : user.description            
        }
        

