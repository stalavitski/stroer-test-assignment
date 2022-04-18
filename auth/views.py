from drf_social_oauth2.views import ConvertTokenView as BaseConvertTokenView
from drf_yasg.utils import swagger_auto_schema

from auth import serializers


class ConvertTokenView(BaseConvertTokenView):
    @swagger_auto_schema(request_body=serializers.ConvertTokenSerializer)
    def post(self, request, *args, **kwargs):
        request.data['grant_type'] = 'convert_token'
        request.data['backend'] = 'google-oauth2'
        return super().post(request, *args, **kwargs)
