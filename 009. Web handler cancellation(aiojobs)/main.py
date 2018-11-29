# 경우에 따라 GET 요청을 처리할 때, 데이터베이스 또는 다른 웹 리소스에서 데이터를 가져오는 경우가 있으므로 가져오는 속도가 느려질 수 있다.
# aiohttp 는 이 과정에서 클라이언트가 커넥션을 끊으면, 시간과 리소스(메모리)를 낭비하지 않기 위해 데이터를 다시 클라이언트로 보내지 않고 커넥션을 캔슬한다.
# 그러나 POST 요청과 같은 경우, 클라이언트의 커넥션 캔슬과 상관없이 데이터를 DB에 저장해야하므로 서버의 커넥션 캔슬은 위험하다.

# aiohttp 의 Web handler cancellation 으로 부터 보호하기 위한 몇가지 방법이 있다.

# DB에 데이터를 저장하는 코루틴에 asyncio.shield() 를 적용한다.
# 이 경우는 핸들러와 async 함수 둘로 분리해야 한다는 단점이 있다.
"""
async def handler(request):
    await asyncio.shield(write_to_redis(request))
    await asyncio.shield(write_to_postgres(request))
    return web.Response(text='OK')
"""
# 위와 같은 경우, shield 를 write_to_redis 에 적용했기 때문에 데이터를 redis 에 저장한 직후에 취소가 발생하면 write_to_postgres 가 호출되지 않는다.

# DB에 데이터를 저장하기 위한 새로운 task 를 생성한다.
# 이경우는 새로운 작업을 await 할 공간이 없으며, 작업이 파괴되지만 보류된다.

# 'aiojobs' 와 같은 서드 파티 라이브러리를 사용한다.
# aiojobs 는 비동기 애플리케이션에 대한 백그라운드 작업 스케줄링을 제어하게 해주는 라이브러리이다.
# 자세한 부분은 third party library 에서 알아보자.
# aiojobs 는 새로운 작업을 생성하고, await 할 수 있게 해준다. 또한, 예약된 모든 작업들 내부 데이터 구조에 저장하고, 우아하게 종료할 수 있다.
# 완료되지 않은 모든 작업들은 'Application.on_cleanup' 신호에서 종료된다.
import asyncio
from aiohttp import web
from aiojobs.aiohttp import setup, spawn, atomic


async def coro(timeout):
    await asyncio.sleep(timeout)


async def handler(request):
    # spawn 함수를 사용하여 cancellation 으로부터 보호
    await spawn(request, coro(3))
    return web.Response(text='using spawn()')


# 전체 핸들러를 cancellation 으로부터 보호하고 싶다면 atomic 데코레이터를 사용
# async function 인 모든 함수가 cancellation 으로부터 보호되므로, write_to_db() 는 중단되지 않는다.
@atomic
async def handler2(request):
    # await write_to_db()
    return web.Response(text='using @atomic')


app = web.Application()
setup(app)
app.router.add_get('/spawn', handler)
app.router.add_post('/atomic', handler2)

web.run_app(app)
