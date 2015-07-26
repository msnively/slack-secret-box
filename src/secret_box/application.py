from flask import Flask
from database import db_session
from models import User, Channel, Message, Retrospective

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

STATUS_TEMPLATE = """<p>Current users: %(user_count)s</p>
<p>Current channels: %(channel_count)s</p>
<p>Current messages: %(message_count)s</p>"""


@app.route("/")
def root():
    data = {
        "user_count": User.query.count(),
        "channel_count": Channel.query.count(),
        "message_count": Message.query.count()
    }
    return STATUS_TEMPLATE % data

if __name__ == "__main__":
    app.run(host='0.0.0.0')