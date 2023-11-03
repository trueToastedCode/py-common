from aiohttp import web

from .healthcheck_server import make_health_check_server

health_check_server = make_health_check_server(web)
