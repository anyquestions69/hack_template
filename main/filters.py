import django_filters
from .models import *
from django.forms.widgets import TextInput, NumberInput

class MemberFilter(django_filters.FilterSet):
    CHOICES = (
        ('asc', 'Возрастанию рейтинга'),
        ('desc', 'Убыванию рейтинга')
    )
    ordering = django_filters.ChoiceFilter(label='Сортировать по', choices=CHOICES, method='filter_by_order')
    def filter_by_order(self, queryset, name, value):
            expression = 'rating' if value == 'asc' else '-rating'
            return queryset.order_by(expression)

    name = django_filters.CharFilter(label='', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Название'} ))
    inn = django_filters.CharFilter(label='', lookup_expr='icontains', widget=NumberInput(attrs={'placeholder': 'Введите ИНН'} ))
    max_price__gt = django_filters.NumberFilter(field_name='max_price', label='', lookup_expr='gt', widget=NumberInput(attrs={'placeholder': 'Цена >'} ))
    max_price__lt = django_filters.NumberFilter(field_name='max_price', label='', lookup_expr='lt', widget=NumberInput(attrs={'placeholder': 'Цена <'} ))
    address = django_filters.CharFilter(label='', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Введите адрес'} ))
    rating__gt = django_filters.NumberFilter(field_name='rating', label='', lookup_expr='gt', widget=NumberInput(attrs={'placeholder': 'Рейтинг <'} ))
    rating__lt = django_filters.NumberFilter(field_name='rating', label='', lookup_expr='lt', widget=NumberInput(attrs={'placeholder': 'Рейтинг <'} ))
    class Meta:
        model = Member
        fields = ['name', 'inn', 'max_price__lt', 'address', 'rating__gt', 'rating__lt']

class ShortFilter(django_filters.FilterSet):
    inn = django_filters.CharFilter(lookup_expr='icontains', label='', widget=TextInput(attrs={'placeholder': 'Введите ИНН'} ))
    class Meta:
        model = Member
        fields = ['inn']
