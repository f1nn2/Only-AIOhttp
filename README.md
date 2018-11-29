# AioHTTP TIL
- aiohttp 의 [공식문서](https://aiohttp.readthedocs.io) 기반 TIL
    - QuickStart
    - Advanced Usage
    - Reference
    - Etc...
   
<pre>
from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def handler(request):
    name = request.match_info.get('name', 'developer')
    return Reponse(text="Hello, " + name)
    
app = web.web.Application()

app.add_routes(routes)
web.run_app(app)
</pre>