from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from . import views


urlpatterns = [
    path("token/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.RegisterView.as_view(), name="auth_register"),
    path("dashboard/", views.dashboard),

    #Todo Urls
    path("todo/<int:user_id>/", views.TodoListView.as_view()),
    path('todo-detail/<int:user_id>/<int:todo_id>/', views.TodoRetrieveView.as_view()),
    path('todo-mark-as-completed/<int:user_id>/<int:todo_id>/', views.TodoMarkAsCompleted.as_view()),

    #Chat Message
    path("my-messages/<user_id>/", views.MyInbox.as_view()), 
    path("get-messages/<sender_id>/<receiver_id>/", views.GetMessages.as_view()), 
    path("send-messages/", views.SendMessage.as_view()),
    

    #Get / Filter Data
    path("profile/<int:pk>/", views.ProfileDetail.as_view()),
    path("search/<username>/", views.SearchUser.as_view()),
]
