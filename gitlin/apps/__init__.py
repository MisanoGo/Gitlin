from typing import List

from aiogram import Router

from . import test_app, notifhub

app_routers: List[Router] = [ 
    test_app.test_route,
    notifhub.ntfy_route
    # register apps here
]

main_route: Router = Router()
main_route.include_routers(*app_routers)
