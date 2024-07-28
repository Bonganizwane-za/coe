from django.shortcuts import render
from django.http import HttpResponse
from flask_chatbot import app as flask_app

def flask_proxy(request):
    with flask_app.test_request_context():
        flask_response = flask_app.dispatch_request()
    return HttpResponse(flask_response.data, content_type=flask_response.mimetype)
