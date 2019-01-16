import coreapi
from rest_framework.filters import BaseFilterBackend


class SwaggerQueryStringFilter(BaseFilterBackend):
    """
    create query string parameter for swagger
    """

    def get_schema_fields(self, view):
        fields = []
        for key, value in view.serializer_class._declared_fields.items():
            field = coreapi.Field(name=key, description=value.help_text, required=value.required, location="query", )
            fields.append(field)
        return fields
