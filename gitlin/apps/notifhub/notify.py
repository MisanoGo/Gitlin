from aiogram import Router
from pyramid import view

from gitlin import utils, db, aiobot

ENDPOINT: str = utils.env_conf["ENDPOINT"]

@view.view_default(route_name=ENDPOINT, renderer="json", request_method="POST")
class GithubWebhookPayload(object):
    def __init__(self, request):
        self.request = request
        self.payload = self.request.json

        self.notif: str = ""
        # TODO: render an template specified by event name


    def renderText(self):
        pass

    def __del__(self):
        data = db.getByRepo(self.payload['']) #TODO: get repo id from payload
        map(lambda d: aiobot.bot.send_message(d["chat"],self.notif,d["thread"]),data)

