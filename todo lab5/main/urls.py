from rest_framework.routers import SimpleRouter

from main.views import TodoListViewSet

router = SimpleRouter()
router.register('todos', TodoListViewSet, basename='todo')

urlpatterns = router.urls
