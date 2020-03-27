from django.shortcuts import render
from django.utils import timezone
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView
#from django_tables2.export.views import ExportMixin
from django_tables2.paginators import LazyPaginator

from .models import Post
from .tables import (
    Expedientes,
)


# Create your views here.
def post_list(request):
    table = Expedientes(
        Post.objects.all().order_by('anio','numexp'), attrs={"class": "paleblue"}, template_name="django_tables2/table.html"
    )
    #posts = Post.objects.all().order_by('anio','numexp') #Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'table': table})
