import django_filters
from .models import Consultation

class ConsultationFilter(django_filters.FilterSet):
    patient = django_filters.NumberFilter(field_name='patient__id', lookup_expr='exact')

    class Meta:
        model = Consultation
        fields = ['patient']