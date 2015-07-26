from flask import Flask
from database import db_session
from models import User, Channel, Message, Retrospective

application = Flask(__name__)


@application.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

STATUS_TEMPLATE = """<p>Current users: %(user_count)s</p>
<p>Current channels: %(channel_count)s</p>
<p>Current messages: %(message_count)s</p>"""


@application.route("/", methods=['GET'])
def root_get():
    data = {
        "user_count": User.query.count(),
        "channel_count": Channel.query.count(),
        "message_count": Message.query.count()
    }
    return STATUS_TEMPLATE % data


@application.route("/", methods=['POST'])
def root_post():
    json = request.get("json")
    if json is None:
        return "No data in request!"


if __name__ == "__main__":
    application.run(host='0.0.0.0')
