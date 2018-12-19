import requests
import json

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAN50YSLZB6ABAJ02J91Ms6KAbZAgNTAGVyGDNpSX589FJVGS9KLCcDpAZBWrzmQoAeAlZBGmZC8D4viPFjuAHGjjd4FYCVH4NZAxKTwdrxzaRxok6IZBfD2ZCr7sQp9ZCA6M0mubMArEL3ZA27NZAZBZASRujZCF1trmYJGOyZCwXO4z5lh5amhZAGxPhub"

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

def send_button_message(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message":{
            "attachment":{
                "type": "template",
                "payload": {
                    "template_type":"button",
                    "text": text,
                    "buttons": buttons
                }
            }
        }
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print("Unable to send message: " + response.text)

    return response
