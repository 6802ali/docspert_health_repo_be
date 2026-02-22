from consultation.ai_service import generate_consultation_summary
from consultation.models import Consultation
from rest_framework import viewsets
from consultation.serializers import ConsultationSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from .filters import ConsultationFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class ConsultationPaginationClass(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

# Create your views here.
class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.select_related("patient").all()
    serializer_class = ConsultationSerializer
    pagination_class = ConsultationPaginationClass
    filter_backends = [DjangoFilterBackend]
    filterset_class = ConsultationFilter

    @action(detail=True, methods=["post"], url_path="generate-summary")
    def generate_summary(self, request, pk=None):
        consultation = self.get_object()

        if not consultation.symptoms:
            return Response(
                {"error": "Cannot generate summary: symptoms field is empty."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if consultation.ai_summary:
            serializer = self.get_serializer(consultation)
            return Response(serializer.data, status=status.HTTP_200_OK)

        try:
            summary = generate_consultation_summary(
                symptoms=consultation.symptoms,
                diagnosis=consultation.diagnosis or "Not yet diagnosed"
            )
            consultation.ai_summary = summary
            consultation.save(update_fields=["ai_summary"])
        except Exception as e:
            return Response(
                {"error": f"AI service failed: {str(e)}"},
                status=status.HTTP_502_BAD_GATEWAY
            )

        serializer = self.get_serializer(consultation)
        return Response(serializer.data, status=status.HTTP_200_OK)