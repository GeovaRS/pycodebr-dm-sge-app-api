from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from . import models, forms, serializers


class InFlowListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView
):
    model = models.InFlow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


class InFlowCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView
):
    model = models.InFlow
    template_name = 'inflow_create.html'
    form_class = forms.InFlowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.add_inflow'


class InFlowDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView
):
    model = models.InFlow
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflow'


class InFlowCreatListAPIView(generics.ListCreateAPIView):
    queryset = models.InFlow.objects.all()
    serializer_class = serializers.InFlowSerializer


class InFlowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.InFlow.objects.all()
    serializer_class = serializers.InFlowSerializer
