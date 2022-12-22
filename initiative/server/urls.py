from django.urls import path

from . import views as _views

urlpatterns = [
    path("signees/", _views.SigneeList.as_view()),
    path("signee/<int:id>", _views.SigneeRetrieve.as_view(), name="signee"),
    path("user/<int:id>", _views.UserRetrieve.as_view(), name="user"),
    path("signature/<int:id>", _views.SignatureRetrieve.as_view(), name="signature"),
    path("initiative/<int:id>", _views.InitiativeRetrieve.as_view(), name="initiative"),
    path("initiatives/", _views.InitiativesList.as_view(), name="initiatives"),
]
