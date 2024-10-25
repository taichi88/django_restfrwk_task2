


from django.urls import path
from note.views import RegisterView, LoginView, Logout, NoteList, NoteDetail

urlpatterns = [
    path("user/register", RegisterView.as_view(), name="register"),
    path("user/login", LoginView.as_view(), name="login"),
    path("user/logout", Logout.as_view(), name="logout"),
    path("notes/", NoteList.as_view(), name="notes"),
    path("notes/<int:pk>", NoteDetail.as_view(), name="notes detail"),

]
