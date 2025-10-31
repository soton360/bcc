from rest_framework import serializers
from bcc_member.models import BCCMember

class BCCMemberSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='role.name', read_only=True)
    class Meta:
        model = BCCMember
        fields = '__all__'