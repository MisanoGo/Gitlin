from typing import List

from aiogram import Router

from . import *


apps_routers: List[Router] = [ 
    test.tst_rt
    # register apps here
]

test_route: Router = Router('test_router')
test_route.include_routers(*apps_routers)
