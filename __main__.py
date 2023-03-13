import logging
import asyncio

from wsgiref.simple_server import make_server
from pyramid.config import Configurator

import aiobot
import utils


ENDPOINT = utils.env_conf["ENDPOINT"]
BOT_TOKEN = utils.env_conf["ENDPOINT"]


def runGithubWebhook(ENDPOINT: str):
    config = Configurator()
    config.add_route(ENDPOINT, "/{}".format(ENDPOINT))
    config.scan()

    app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 80, app)
    server.serve_forever()

def runAioGram(BOT_TOKEN: str):
    logging.basicConfig(level=logging.INFO)
    asyncio.run(aiobot.fire(BOT_TOKEN))

if __name__ == "__main__":
    runAioGram(BOT_TOKEN)
    runGithubWebhook(ENDPOINT)
