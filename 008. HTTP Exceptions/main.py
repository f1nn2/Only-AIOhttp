from aiohttp import web

# aiohttp 에서는 모든 HTTP 예외에 대한 상태코드를 정의해 놓았다.
# 모든 exceptions 의 조상인 HTTPException 은 web.Response 와 Exception 을 상속 받는다.


async def response_404(request):
    # 모든 HTTP exceptions 의 생성사 시그니처는 이렇다. (*, headers=None, reason=None, body=None, text=None, content_type=None)
    return web.HTTPNotFound()


async def response_302(request):
    # 300, 301, 302, 303, 305, 306, 307 은 생성자에 'location' 인자를 넣어주어야 한다. location 은 Location HTTP header 의 값이다.
    # '/founded-resource' 를 임시 이동 location 으로 하여 이곳으로 redirect 된다.
    return web.HTTPFound('/founded-resource')


async def response_405(request):
    # 405 를 표현하는 HTTPMethodNotAllowed 는 허용하지 않는 메서드와 허용하는 메서드의 집합을 생성자에 넣어야 한다.
    return web.HTTPMethodNotAllowed('POST', ['GET', 'HEAD', 'PUT'])


async def some_resource(request):
    return web.Response(text='Found resource here', status=200)


async def create_app():
    app = web.Application()
    app.add_routes([web.get('/not-found', response_404),
                    web.get('/found', response_302),
                    web.post('/method-not-allowed', response_405),
                    web.get('/founded-resource', some_resource)])

    return app

web.run_app(create_app())
