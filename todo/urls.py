from django.urls import path, include
from rest_framework import routers

from .views import (
    todo_list_create,
    todo_detail,
    Todos,
    TodoDetail,
    TodoMVS
    )

router = routers.DefaultRouter()
router.register('task', TodoMVS)

urlpatterns = [
    # path('list-create/', todo_list_create),
    # path('detail/<int:id>', todo_detail),
    # path('list-create/', Todos.as_view()),
    # path('detail/<int:pk>', TodoDetail.as_view()),
    path('', include(router.urls))
]
