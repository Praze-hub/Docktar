from .utils.nlp import analyze_symptom, translate_text
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import SymptomInputSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class SymptomInputViewSet(viewsets.ViewSet):
    serializer_class = SymptomInputSerializer

    @swagger_auto_schema(
        method='post',
        request_body=SymptomInputSerializer,
        responses={200: openapi.Response('Success')}
    )
    @action(
        detail=False,
        methods=['post'],
        url_path='analyze'
    )
    def analyze_symptom_action(self, request):
        serializer = SymptomInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        symptom = serializer.validated_data['symptom']
        language = serializer.validated_data.get('language', 'en')

        advice = analyze_symptom(symptom)
        if language and language.lower() != 'en':
            advice = translate_text(advice, language)

        return Response(
            {'advice': advice},
            status=status.HTTP_200_OK
        )

