import logging
import asyncio

from wsgiref.simple_server import make_server
from pyramid.config import Configurator

import aiobot
import utils


ENDPOINT = utils.env_conf["ENDPOINT"]


def runGithubWebhook(ENDPOINT: str):
    # start ENDPOINT listener
    config = Configurator()
    config.add_route(ENDPOINT, "/{}".format(ENDPOINT))
    config.scan()

    # start server for gat the webhooks
    app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 80, app)
    server.serve_forever()

def runAioGram(bot,BOT_TOKEN: str):
    # start telegram bot poller
    logging.basicConfig(level=logging.INFO)
    asyncio.run(aiobot.fire(bot,BOT_TOKEN))

if __name__ == "__main__":
    runAioGram(aiobot.bot,aiobot.BOT_TOKEN)
    runGithubWebhook(ENDPOINT)
