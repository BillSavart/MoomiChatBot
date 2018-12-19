import requests
import json

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAN50YSLZB6ABACZA8g7H1ZBaDYUOiQnIe2TCPSZB8QGQypRVqUeSa3ZAOP6cQK1TOvG5kjenanLqCZCZCNuUqCQmz2Qm06mwiewKPu2uZB7gHZAWggdwUkR0ZATm907QzjpSdU2N7ClIXF5lMskIkwrkFZChvvoQYoTynz2piCeG4lFb1GBX9ndU2f"

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_img_message(fb_id, image_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    response = {
        "attachment": {
            "type": "image",
            "payload": {
                "url": image_url,
                "is_reusable": True
            },
        }
    }
    response_msg = json.dumps({"recipient": {"id": fb_id}, "message": response})
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=response_msg)

    if response.status_code != 200:
        print("Unable to send image message")

    return response

"""
def send_button_message(id, text, buttons):
    pass
"""
