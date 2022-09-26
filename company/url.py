from django.urls import re_path
from .views import (
    collectionView

)

urlpatterns = [
    re_path(r'^company/$', collectionView.as_view()),
    # re_path(r'^company/?([0-9]+)$', collectionView.as_view()),
    re_path(r'^company/name/(^[A-Za-z0-9-]*$)$', collectionView.as_view()),

    # re_path(r'')
]
