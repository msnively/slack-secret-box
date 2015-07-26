from flask import Flask
application = Flask(__name__)

@application.route("/")
def root():
    return "Testing, testing..."

if __name__ == "__main__":
    application.run(host='0.0.0.0')