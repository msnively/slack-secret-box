from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Interval
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import ArrowType
import arrow

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slack_id = Column(String)
    messages = relationship("Message", backref="user")

    def __init__(self, name=None, slack_id=None):
        self.name = name
        self.slack_id = slack_id

    def __repr__(self):
        return "<User %r>" % self.name

    def __str__(self):
        return "<User %r>" % self.name


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slack_id = Column(String)
    messages = relationship("Message", backref="channel")

    def __init__(self, name=None, slack_id=None):
        self.name = name
        self.slack_id = slack_id

    def __repr__(self):
        return "<Channel %r>" % self.name

    def __str__(self):
        return "<Channel %r>" % self.name


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    created_at = Column(ArrowType)
    text = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    channel_id = Column(Integer, ForeignKey('channels.id'))

    def __init__(self, text=None, user_id=None, channel_id=None):
        self.text = name
        self.user_id = user_id
        self.channel_id = channel_id
        self.created_at = arrow.utcnow()

    def __repr__(self):
        return "<Message by %r at %r>" % (self.user, self.created_at)

    def __str__(self):
        return "<Message by %r at %r>" % (self.user, self.created_at)


class Retrospective(Base):
    __tablename__ = "retrospectives"

    id = Column(Integer, primary_key=True)
    start_time = Column(ArrowType)
    frequency = Column(ArrowType)
