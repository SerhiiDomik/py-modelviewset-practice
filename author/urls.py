from django.urls import path, include
from rest_framework.routers import DefaultRouter

from author.views import AuthorViewSet

# router = DefaultRouter()
# router.register(r'authors', AuthorViewSet, basename='author')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

app_name = "author"

author_list = AuthorViewSet.as_view(actions={"get": "list", "post": "create"})

author_detail = AuthorViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("actors/", author_list, name="actor_list"),
    path("actors/<int:pk>/", author_detail, name="actor_detail"),
]
