# -*- coding: utf-8 -*-
"""
    flaskbb.forum.forms
    ~~~~~~~~~~~~~~~~~~~~

    It provides the forms that are needed for the forum views.

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
from flask.ext.wtf import Form
from wtforms import TextAreaField, TextField
from wtforms.validators import Required

from flaskbb.forum.models import Topic, Post, Report


class QuickreplyForm(Form):
    content = TextAreaField("Quickreply", validators=[
        Required(message="You cannot post a reply without content.")])

    def save(self, user, topic):
        post = Post(**self.data)
        return post.save(user=user, topic=topic)


class ReplyForm(Form):
    content = TextAreaField("Content", validators=[
        Required(message="You cannot post a reply without content.")])

    def save(self, user, topic):
        post = Post(**self.data)
        return post.save(user=user, topic=topic)


class NewTopicForm(ReplyForm):
    title = TextField("Topic Title", validators=[
        Required(message="A topic title is required")])
    content = TextAreaField("Content", validators=[
        Required(message="You cannot post a reply without content.")])

    def save(self, user, forum):
        topic = Topic(title=self.title.data)
        post = Post(content=self.content.data)
        return topic.save(user=user, forum=forum, post=post)


class ReportForm(Form):
    reason = TextAreaField("Reason", validators=[
        Required(message="Please insert a reason why you want to report this \
                          post")
    ])

    def save(self, user, post):
        report = Report(**self.data)
        return report.save(user, post)
