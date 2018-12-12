from aiohttp import web

# 사실 정적 파일을 처리하는 가장 좋은 방법은 Nginx 나 CDN service 같은 Reverse Proxy 를 사용하는 것이다.
# 그러나 개발을 위해 정적 파일을 aiohttp app 자체에서 처리하는 것은 매우 편리해서 알아둘 필요가 있다.


async def file_handler(request):
    # 가장 간단하게 파일 리스폰스를 하는 방법
    return web.FileResponse('./imgs/asdf.jpg')


app = web.Application()

app.add_routes([web.get('/image/asdf', file_handler),

                # 단지 static route 를 등록하려면 .static() 을 이용
                web.static('/file', './imgs',

                           # 브라우저에서 직접적으로 정적 라우트 디렉터리에 접근했을 때, aiohttp 는 기본적으로 403을 리턴한다.
                           # 만약, 직접 접근했을때 디렉토리 인덱스를 허용하고 싶다면
                           show_index=True,

                           # 정적 디렉토리에서 symlink 에 접근하면 기본적으로 404 를 리턴하기 때문에 follow_symlinks 옵션을 True 로
                           # symlink : 심볼릭 링크는 절대-상대 경로 형태로 된 다른 파일이나 디렉터리에 대한 참조를 포함하고 있는 특별한 파일
                           # (여기서 '링크' 는 파일시스템에서 링크를 말하는 것이며, 하드 링크와 심볼릭 링크로 나뉘고 대표적 예로 바로가기가 있다.)
                           # (하드 링크는 같은 파일시스템에서만 사용가능 <= 파일시스템에서의 고유 번호로 연결하기 때문에 다른 파일시스템 참조 불가)
                           # (심볼릭 링크는 파일의 경로를 가지고 참조하기 때문에 다른 파일 시스템에서도 사용 가능)
                           follow_symlinks=True,

                           # Cache busting 을 원한다면 append_version 옵션을 True 로 해야한다.
                           # Cache busting 이란, 리소스 파일 이름(css, js, etc...)에 파일 버전 해쉬를 추가하는 과정이다.
                           # 이를 사용함으로써 얻을 수 있는 성능적 이점은, 파일이 변경될 때, 클라이언트가 최신 버전을 가져오지 못하는 것에 대해
                           # 걱정없이 브라우저가 해당 파일을 무기한으로 캐시할 수 있다는 것이다.
                           append_version=True)])

web.run_app(app)
