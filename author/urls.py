from django.urls import path

from author.views import AuthorViewSet

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
    path("actors/", author_list, name="manage-list"),
    path("actors/<int:pk>/", author_detail, name="manage-detail"),
]
