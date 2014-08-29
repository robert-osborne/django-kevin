from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()
