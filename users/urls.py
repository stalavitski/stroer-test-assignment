from rest_framework import routers

from users import views

app_name = 'users'

router = routers.SimpleRouter()
router.register('users', views.UserViewSet, basename='User')
urlpatterns = router.urls
