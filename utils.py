import requests
import json

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAN50YSLZB6ABAMmDRfTSQ5I80CrVAmanhrlM1QaGZCkJNPF5OWO2CpIy5M1AK3IFPsbGekQqOJHv5fd0SZCZCd88VZBZC9BccQn4T6k8WQgMId7ZByZAfolS2BHLR4h6AdutEqLMa66pJVU8yLIRcSMhOBYzCKDIUXVf9DkaK4uZAIHRHTvtRV5r"

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
