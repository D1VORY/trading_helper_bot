from websocket import WebSocketApp
from settings import bot


class OrderListener(WebSocketApp):

    def __init__(self):
        super().__init__(
            url='',
            on_open=OrderListener.on_open,
            on_message=OrderListener.on_message,
            on_error=OrderListener.on_error,
            on_close=OrderListener.on_close
        )

    @staticmethod
    def on_open(ws):
        print('Websocket opened!!!!!!!')
        pass

    @staticmethod
    def on_message(ws, message):
        print(message)

    @staticmethod
    def on_error(ws, error):
        print(error)

    @staticmethod
    def on_close(ws):
        print("### closed ###")