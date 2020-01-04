from src.bot.messages import Answer, BotAnswer, BotMessage
from src.bot.text import Text, InputText
from src.server import server, Request, ServerRequest


@server.route("/", methods=("GET", "POST"))
def index():
    request: Request = ServerRequest()
    answer: Answer = BotAnswer(request)

    if request.method() == "POST":
        text: Text = InputText(answer.message())

        if text.match():
            BotMessage(answer.chat_id(), text.get()).send()

    return server.render_template("index.html")
