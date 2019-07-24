"""
需求账号已登录阻止再次登录
仿照https://github.com/pcraston/django-preventconcurrentlogins写一个中间件
如果账号已登录最后return登录页面
顶替原先的登录只需要删除原先的session就行了，而阻止再次登录需要考虑什么时候用户想session失效
同时设置 SESSION_EXPIRE_AT_BROWSER_CLOSE = True ，SESSION_COOKIE_AGE = 60 * 15
"""
from django.http import HttpResponse

def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # response = get_response(request)
        response = HttpResponse()

        # Code to be executed for each request/response after
        # the view is called.
        response.content = u'账号已登录，禁止再次登录'
        return response

    return middleware