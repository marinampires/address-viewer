from rest_framework import serializers
from addresses_viewer.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address        