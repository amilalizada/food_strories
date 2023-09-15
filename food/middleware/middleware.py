from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

class CustomMiddleware(MiddlewareMixin):
    black_list = [
        
    ]
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.black_list:
            return HttpResponseForbidden('<h1>Forbidden</h1>')
        