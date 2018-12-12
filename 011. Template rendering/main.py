from aiohttp import web
import aiohttp_jinja2
import jinja2

routes = web.RouteTableDef()

# aiohttp 는 별도의 설치가 필요없는 템플릿 엔진을 지원하지 않는다.
# 그러나 jinja2 템플릿 엔진을 사용할 수 있는 서드 파티 라이브러리 aiohttp_jinja2 가 있다!!


# 간편하게 .tempate() 데코레이터로 렌더링할 수 있다!!
# .template() 로 핸들러를 wrap 할때는 당연히 라우팅 데코레이터 다음으로 사용해야한다.
@routes.get('/index')
@aiohttp_jinja2.template('index.html')
async def handler(request):
    # jinja2 에서 쓸 변수에 값을 줄 때는 다음과 같이 k:v 형태로 사용한다.
    return {'name': 'flouie'}

app = web.Application()

# jinja2 환경을 셋
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./templates'))

app.add_routes(routes)
web.run_app(app)
