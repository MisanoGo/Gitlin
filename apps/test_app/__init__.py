from typing import List

from aiogram import Router

from . import test


apps_routers: List[Router] = [ 
    test.tst_rt
    # register apps here
]

test_route: Router = Router()
test_route.include_routers(*apps_routers)
