from  MZI.serializers import BaseModelSerializer
from Account.models import AdminMZI
class AdminMZISerializer(BaseModelSerializer):
    class Meta:
        model = AdminMZI
        fields =  (
            'first_name',
            'last_name',
            'role_name',
            'profile_image',
        )