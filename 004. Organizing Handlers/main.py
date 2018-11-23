from aiohttp import web


# aiohttp.web은 구현 세부 사항을 강요(구술)하지 않으므로, 개발자가 원한다면 클래스로 logically similar 한 핸들러들을 클래스로 묶을 수 있다.
class Handler:
    def __init__(self):
        pass

    async def handler_greeting(self, request):
        name = request.match_info['name']
        res = 'Hi, {}'.format(name)
        return web.Response(text=res)

    async def handler_say_goodbye(self, request):
        return web.Response(text='Good bye')


app = web.Application()

# 인스턴스를 생성하고
handler = Handler()
# 핸들러 메서드를 라우팅한다.
app.add_routes([web.get('/{name}/greeting',  handler.handler_greeting),
                web.get('/bye', handler.handler_say_goodbye)])

web.run_app(app)
