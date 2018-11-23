from aiohttp import web

routes = web.RouteTableDef()


# flask 에서는 third party 인 flask-restful 을 사용하여 class based view 를 구현했지만
# aiohttp 는 자체에서 class based view 를 지원한다
@routes.view('/path')
class ClassBasedView(web.View):
    # aiohttp.web.RouteTableDef.get()
    async def get(self):
        return web.Response(text='get')

    # aiohttp.web.RouteTableDef.post()
    async def post(self):
        return web.Response(text='post')


app = web.Application()
app.router.add_routes(routes)
web.run_app(app)
