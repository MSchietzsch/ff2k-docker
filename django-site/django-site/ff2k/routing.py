from channels.routing import ProtocolTypeRouter
from channels.consumer import SyncConsumer


application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
})

class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })
