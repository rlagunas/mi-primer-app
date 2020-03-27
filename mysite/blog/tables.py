import django_tables2 as tables

from .models import Post

class Expedientes(tables.Table):

    class Meta:
        model = Post
        fields = ("numexp", "anio", "quejoso", "fecarc", "tipo","created_date")
        template_name = "django_tables2/bootstrap.html"
