from django.urls import path
from . views import sign_up_view, sign_in_view, delete_user_view, sign_out_view, hello_view


urlpatterns = [
    path('sign_up/', sign_up_view, name='sign_up'),
    path('sign_in/', sign_in_view, name='sign_in'),
    path('delete_user/', delete_user_view, name='delete_user'),
    path('sign_out/', sign_out_view, name='sign_out'),
]
