from django.utils.deprecation import MiddlewareMixin

class TaskMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('请求处理')

    def process_response(self, request, response):
        print('响应处理')
        return response