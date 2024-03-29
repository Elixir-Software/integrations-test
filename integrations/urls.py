"""integrations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from core import models


class FieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Field
        fields = "__all__"

class FieldViewSet(viewsets.ModelViewSet):
    queryset = models.Field.objects.all()
    serializer_class = FieldSerializer

class FormSerializer(serializers.HyperlinkedModelSerializer):
    def get_field(self, obj):
        return obj.field

    class Meta:
        model = models.Form
        fields = ["object", "field", "value"]

class FormViewSet(viewsets.ModelViewSet):
    queryset = models.Form.objects.all()
    serializer_class = FormSerializer

class IntegerFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.IntegerForm
        fields = ["object", "field", "value"]

class IntegerFormViewSet(viewsets.ModelViewSet):
    queryset = models.IntegerForm.objects.all()
    serializer_class = IntegerFormSerializer

class FloatFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FloatForm
        fields = ["object", "field", "value"]

class FloatFormViewSet(viewsets.ModelViewSet):
    queryset = models.FloatForm.objects.all()
    serializer_class = FloatFormSerializer

class CharacterFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CharacterForm
        fields = ["object", "field", "value"]

class CharacterFormViewSet(viewsets.ModelViewSet):
    queryset = models.CharacterForm.objects.all()
    serializer_class = CharacterFormSerializer

class TextFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TextForm
        fields = ["object", "field", "value"]

class TextFormViewSet(viewsets.ModelViewSet):
    queryset = models.TextForm.objects.all()
    serializer_class = TextFormSerializer

class BooleanFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BooleanForm
        fields = ["object", "field", "value"]

class BooleanFormViewSet(viewsets.ModelViewSet):
    queryset = models.BooleanForm.objects.all()
    serializer_class = BooleanFormSerializer

class DateFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DateForm
        fields = ["object", "field", "value"]

class DateFormViewSet(viewsets.ModelViewSet):
    queryset = models.DateForm.objects.all()
    serializer_class = DateFormSerializer

class URLFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.URLForm
        fields = ["object", "field", "value"]

class URLFormViewSet(viewsets.ModelViewSet):
    queryset = models.URLForm.objects.all()
    serializer_class = URLFormSerializer

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    field_set = FieldSerializer(many=True)

    class Meta:
        model = models.Service
        fields = ["name", "description", "field_set"]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = ServiceSerializer

class ObjectSerializer(serializers.HyperlinkedModelSerializer):
    service = ServiceSerializer()
    form_set = FormSerializer(many=True)

    class Meta:
        model = models.Object
        fields = ["pk", "human_id", "service", "form_set"]

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = models.Object.objects.all()
    serializer_class = ObjectSerializer


router = routers.DefaultRouter()
router.register("objects", ObjectViewSet)
router.register("services", ServiceViewSet)
router.register("boolean_forms", BooleanFormViewSet)
router.register("text_forms", TextFormViewSet)
router.register("character_forms", CharacterFormViewSet)
router.register("float_forms", FloatFormViewSet)
router.register("integer_forms", IntegerFormViewSet)
router.register("date_forms", DateFormViewSet)
router.register("url_forms", URLFormViewSet)
router.register("forms", FormViewSet)
router.register("fields", FieldViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("customer-api/", include("core.urls")),
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls")),
]
