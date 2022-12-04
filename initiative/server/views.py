from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import models as _models
from . import serializers as _ser
from . import permissions as _perms


# Create your views here.


class SigneeList(generics.ListCreateAPIView):
    serializer_class = _ser.SigneeSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return _models.Signee.objects.filter(user=self.request.user)


class UserRetrieve(generics.RetrieveAPIView):
    serializer_class = _ser.UserSerializer
    permission_classes = [IsAuthenticated, _perms.CanRetrieveUserPermission]
    lookup_field = "id"

    def get_queryset(self):
        pk = self.kwargs["id"]
        return _models.User.objects.filter(id=pk)


class SignatureRetrieve(generics.RetrieveAPIView):
    serializer_class = _ser.SignatureSerializer
    permission_classes = [IsAuthenticated, _perms.CanRetrieveSignaturePermission]
    lookup_field = "id"

    def get_queryset(self):
        pk = self.kwargs["id"]
        return _models.Signature.objects.filter(id=pk)


class InitiativeRetrieve(generics.RetrieveAPIView):
    queryset = _models.Initiative.objects.all()
    serializer_class = _ser.InitiativeSerializer
    lookup_field = "id"
