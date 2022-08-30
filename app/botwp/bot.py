from flask import Blueprint, request;
import requests
from twilio.twiml.messaging_response import MessagingResponse;

bp_bots = Blueprint('bot', __name__);

@bp_bots.route('/bot', methods=['POST'])
def start():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("Olá, como posso te ajudar ?")
    return str(resp);