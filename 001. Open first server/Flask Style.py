from aiohttp import web

# 이번에는 route table class 를 이용하여 flask 의 decorator 방식으로 라우팅한다.
# RouteTableDef 는 router 들을 담는 list 와 비슷한 시퀀스이다.
routes = web.RouteTableDef()


@routes.get('/')
async def say_hello(request):
    return web.Response(text='hello, aiohttp')


app = web.Application()

# 시퀀스에 담긴 라우터들을 애플리케이션의 라우터로 등록한다.
app.add_routes(routes)
web.run_app(app)
