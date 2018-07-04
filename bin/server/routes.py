from bin.bot.messages import Answer, BotAnswer, BotMessage
from bin.bot.text import Text, InputText
from bin.server import SERVER, METHODS, Request, ServerRequest, POST, WELCOME_MESSAGE, Server

_server: Server = SERVER


@_server.route('/', methods=METHODS)
def index():
    request: Request = ServerRequest()
    answer: Answer = BotAnswer(request)

    if request.method() == POST:
        text: Text = InputText(answer.message())

        if text.match():
            BotMessage(answer.chat_id(), text.get()).send()

    return WELCOME_MESSAGE
