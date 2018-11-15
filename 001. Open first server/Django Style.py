from aiohttp import web

# aiohttp 로 첫 서버를 열어보자
# django 의 'urls.py' 방식이다.


# handler 는 aiohttp.web.Request 의 인스턴스를 인자로 받으며, StreamResponse 를 상속받는 클래스의 인스턴스를 반환하는 코루틴이어야 한다.
async def say_hello(request):
    return web.Response(text='Hello, aiohttp')


async def no_head(request):
    return web.Response(text='only get method')


async def wildcard_http_method(request):
    return web.Response(text='this router allows all HTTP method')

# aiohttp web application instance 생성
app = web.Application()

# register router
# 여러 method 를 allow 하는 registering routers 의 경우, 같은 path 를 묶어서 등록하는 것이 최적화된다.
app.add_routes([web.get('/', say_hello),

                # 모든 GET 요청이 가능한 endpoint 는 HEAD 로도 요청이 가능하므로, HEAD 요청시 405 를 반환하기 위해 allow_head 옵션을 사용
                web.get('/get', no_head, allow_head=False),

                # 모든 http method 에 대해 서빙하는 라우터는 다음과 같이 추가한다.
                web.route('*', '/all', wildcard_http_method)])

# run at localhost:8080
web.run_app(app)
