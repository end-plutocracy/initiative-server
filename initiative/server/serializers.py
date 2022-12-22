from rest_framework import serializers

from . import models as _models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = _models.User
        fields = ["url", "username", "first_name", "last_name"]
        extra_kwargs = {"url": {"view_name": "user", "lookup_field": "id"}}


class InitiativeSerializer(serializers.HyperlinkedModelSerializer):
    number_of_signatures = serializers.IntegerField()

    class Meta:
        model = _models.Initiative
        fields = ["url", "title", "number_of_signatures"]
        extra_kwargs = {"url": {"view_name": "initiative", "lookup_field": "id"}}


class SignatureSerializer(serializers.HyperlinkedModelSerializer):
    initiative = InitiativeSerializer()
    signed_on = serializers.DateTimeField()

    class Meta:
        model = _models.Signature
        fields = ["url", "initiative", "signed_on"]
        extra_kwargs = {
            "url": {"view_name": "signature", "lookup_field": "id"},
            "initiative": {"view_name": "initiative", "lookup_field": "id"},
        }


class SigneeSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    signatures = SignatureSerializer(many=True)

    class Meta:
        model = _models.Signee
        fields = ["url", "user", "signatures"]
        extra_kwargs = {
            "user": {"view_name": "user", "lookup_field": "id"},
            "signatures": {"view_name": "signature", "lookup_field": "id"},
            "url": {"view_name": "signee", "lookup_field": "id"},
        }
