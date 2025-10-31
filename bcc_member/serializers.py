from rest_framework import serializers
from bcc_member.models import BCCMember
from role.serializers import RoleSerializer

class BCCMemberSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    class Meta:
        model = BCCMember
        fields = '__all__'