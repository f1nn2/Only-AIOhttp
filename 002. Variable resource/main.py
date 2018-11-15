from aiohttp import web

routes = web.RouteTableDef()


# variable resource 를 다뤄보자
# aiohttp 에서는 path parameter 를 받을 때, {} 안에 해당 parameter 의 이름을 넣어 라우팅한다.
@routes.get('/{name}')
async def variable_handler(request):

    # path parameter 의 값을 가져올 때는 request 의 match_info 를 사용하여 가져온다.
    return web.Response(text='Hello, {}'.format(request.match_info['name']))


app = web.Application()
app.add_routes(routes)
web.run_app(app)
