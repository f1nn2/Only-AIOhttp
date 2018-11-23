from aiohttp import web

routes = web.RouteTableDef()


# Aiohttp 는 JSON response 를 위한 손쉬운 방법을 제공한다.
@routes.get('/json/{val}')
async def json_response(request):
    res = {'key': request.match_info['val']}

    # aiohttp.web.json_response()
    return web.json_response(res, status=200)

app = web.Application()
app.add_routes(routes)
web.run_app(app)
