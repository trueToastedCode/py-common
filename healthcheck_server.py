def make_health_check_server(web):
    async def health_check_server(get_is_healthy, host='0.0.0.0', port=3000):
        async def health_check(request):
            if request.path == '/healthcheck':
                return web.Response(status=200 if get_is_healthy() else 500)
            return web.Response(status=404)

        app = web.Application()
        app.router.add_get('/{path:.*}', health_check)

        runner = web.AppRunner(app)
        await runner.setup()

        site = web.TCPSite(runner, host, port)
        await site.start()

    return health_check_server
