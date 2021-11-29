"""
需求账号已登录阻止再次登录
仿照https://github.com/pcraston/django-preventconcurrentlogins写一个中间件
如果账号已登录最后return登录页面
顶替原先的登录只需要删除原先的session就行了，而阻止再次登录需要考虑什么时候用户想session失效
同时设置 SESSION_EXPIRE_AT_BROWSER_CLOSE = True ，SESSION_COOKIE_AGE = 60 * 15
登录时还需要对比session model
"""
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin


# def simple_middleware(get_response):
#     # One-time configuration and initialization.
#
#     def middleware(request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#
#         # response = get_response(request)
#         response = HttpResponse()
#
#         # Code to be executed for each request/response after
#         # the view is called.
#         response.content = u'账号已登录，禁止再次登录'
#         print(User.objects.all())
#         return response
#
#     return middleware


class SimpleMiddleware(MiddlewareMixin):
    # def __init__(self, get_response=None):
    # def process_request(self, request):
    # def process_response(self, request, response):

    def __init__(self, get_response=None):
        self.get_response = get_response
    # def __init__(self):
        print(111111111)

    def process_request(self, request):
        print(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(view_func, view_args, view_kwargs)

    def process_template_response(self, request, response):
        print(response)
        return response

    def process_response(self, request, response):
        print(response)
        return response

    def process_exception(self, request, exception):
        print('exception')
        return HttpResponse('exception')




