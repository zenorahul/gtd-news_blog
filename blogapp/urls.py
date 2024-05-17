from blogapp.views import newsView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('articles',newsView,basename='ArticleS')
urlpatterns=router.urls