import base64
from cryptography import fernet
from aiohttp import web
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage


# 여러 요청에 걸쳐 사용자 데이터를 저장할 공간이 필요한 경우가 많다. 보통 이를 세션이라 한다.
# aiohttp 자체에서는 세션을 제공해 주지 않는다. 그러나, 서드파티 라이브러리인 aiohttp_session 를 사용하면 세션을 사용할 수 있다.

async def handler(request):
    # 'request' 를 get_session 에 전달하면, 해당 리퀘스트 객체에서 가져올 수 있는 세션정보를 반환해준다.
    session = await get_session(request)

    # 마지막으로 방문한 사용자를 response
    last_visit = session['last_visit'] if 'last_visit' in session else None
    text = 'Last visitor is {}'.format(last_visit)
    return web.Response(text=text)


async def make_app():
    app = web.Application()

    # fernet 을 사용하여 세션을 암호화할 대칭키 생성
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))

    app.add_routes([web.get('/', handler)])
    return app

web.run_app(make_app())
