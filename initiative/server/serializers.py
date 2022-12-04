from rest_framework import serializers

from . import models as _models


class SigneeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = _models.Signee
        fields = ["user", "signatures"]
        extra_kwargs = {
            "user": {"view_name": "user", "lookup_field": "id"},
            "signatures": {"view_name": "signature", "lookup_field": "id"},
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = _models.User
        fields = ["username", "first_name", "last_name"]


class SignatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = _models.Signature
        fields = ["initiative", "signed_on"]
        extra_kwargs = {"initiative": {"view_name": "initiative", "lookup_field": "id"}}


class InitiativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = _models.Initiative
        fields = ["title"]
