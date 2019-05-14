import json
from rest_framework.renderers import JSONRenderer

class IntermediarioJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, media_type=None, renderer_context=None):
        
        return json.dumps({ 'Intermediario': data})