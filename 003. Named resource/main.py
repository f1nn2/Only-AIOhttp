from aiohttp import web


routes = web.RouteTableDef()


# named resource 를 생성핧 때는 다음과 같이 url 옆에 키워드 인자로 네이밍 해준다
@routes.get('/{user}/info', name='user-info')
async def handler_with_name(request):
    # 이름으로 resource 를 컨트롤
    url = request.app.router['user-info'].url_for(user='flouie').with_query("a=b")

    # /flouie/info?a=b
    print(url)

    return web.Response(text="this is {}'s information".format(request.match_info['user']))


app = web.Application()
app.add_routes(routes)
web.run_app(app)
