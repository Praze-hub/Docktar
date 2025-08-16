from rest_framework.routers import DefaultRouter
from .views import SymptomInputViewSet

router = DefaultRouter()
router.register(r'chatbot/symptom/analyze', SymptomInputViewSet, basename='symptom')

urlpatterns = router.urls