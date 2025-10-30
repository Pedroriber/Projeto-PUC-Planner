import os
from django.conf import settings
from django.http import FileResponse, Http404

class StaticFilesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        
        if path.endswith('.css') or path.endswith('.js'):
            file_path = os.path.join(settings.BASE_DIR, 'Telas', path.lstrip('/'))
            if os.path.exists(file_path):
                return FileResponse(open(file_path, 'rb'))
        
        if path.startswith('/Recursos de Estilo/'):
            file_path = os.path.join(settings.BASE_DIR, path.lstrip('/'))
            if os.path.exists(file_path):
                return FileResponse(open(file_path, 'rb'))
        
        return self.get_response(request)
