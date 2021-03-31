from django.urls import path
from . import views
# from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('user/', views.uesr_view),

    path('update/', views.UpdateView.as_view()),  # by old pass

    # path('password/change/', ),# by old pass
    # path('password/reset/', ), # by email
    # path('reset/confirm/', ),  # from email
    # path('register/verify-email/', ),

    # path('register/google/', ),
]
