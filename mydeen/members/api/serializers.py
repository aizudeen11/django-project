# turn python object to json
from rest_framework.serializers import ModelSerializer
from members.models import Member

class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'