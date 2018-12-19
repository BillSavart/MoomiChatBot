from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_img_message
from utils import send_button_message

from random import randint
import json

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '嗨'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '抽姆咪'
        return False
    
    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '我們一起學貓叫'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '在你面前撒個嬌'
        return False

    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '我的心臟蹦蹦跳'
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '你不說愛我我就喵喵喵'
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '我想要女主人'
        return False

    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '測驗'
        return False

    def is_going_to_state9(self, event):
        if event.get("postback"):
            text = event['postback'].get('payload')
            return text == 'Python'
        return False

    def is_going_to_state10(self, event):
        if event.get("postback"):
            text = event['postback'].get('payload')
            return text == 'Java'
        return False
    
    def is_going_to_state11(self, event):
        if event.get("postback"):
            text = event['postback'].get('payload')
            return text == 'C++'
        return False
    
    def is_going_to_state12(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text != '在你面前撒個嬌':
                return True
        return False

    def is_going_to_state13(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text != '我的心臟蹦蹦跳':
                return True
        return False

    def is_going_to_state14(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text != '你不說愛我我就喵喵喵':
                return True
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1 for intro")

        sender_id = event['sender']['id']
        intro_text = "嗨, 我是姆咪, 我是一隻四個月大的虎班貓\n人家是女森喔！嘻嘻 ><\n這是我的instagram, 去追蹤一下吧！ https://www.instagram.com/moomi.the.cat\n你可以輸入以下指令：\n1.抽姆咪\n2.我們一起學貓叫\n3.我想要女主人\n4.測驗"
        responese = send_text_message(sender_id, intro_text)
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1 for intro') 

    def on_enter_state2(self, event):
        print("I'm entering state2 for pick")

        sender_id = event['sender']['id']

        random_num = randint(0, 13)

        if random_num == 0: 
            url_msg = "https://i.imgur.com/TUOixeC.jpg"
        elif random_num == 1:
            url_msg = "https://i.imgur.com/sdIMAOA.jpg"
        elif random_num == 2:
            url_msg = "https://i.imgur.com/WPFD5QP.jpg"
        elif random_num == 3:
            url_msg = "https://i.imgur.com/enlHJaI.jpg"
        elif random_num == 4:
            url_msg = "https://i.imgur.com/pnFWIEN.jpg"
        elif random_num == 5:
            url_msg = "https://i.imgur.com/PCfYNcG.jpg"
        elif random_num == 6:
            url_msg = "https://i.imgur.com/XJUFNk2.jpg"
        elif random_num == 7:
            url_msg = "https://i.imgur.com/qfpxJZ4.jpg"
        elif random_num == 8:
            url_msg = "https://i.imgur.com/VXLKxpN.jpg"
        elif random_num == 9:
            url_msg = "https://i.imgur.com/BxkPfy0.jpg"
        elif random_num == 10:
            url_msg = "https://i.imgur.com/9kOZPkl.jpg"
        elif random_num == 11:
            url_msg = "https://i.imgur.com/Sbz9o8K.jpg"
        elif random_num == 12:
            url_msg = "https://i.imgur.com/lAyt569.jpg"
        elif random_num == 13:
            url_msg = "https://i.imgur.com/LWssGRk.jpg"
        else:
            url_msg = "https://i.imgur.com/PCfYNcH.jpg"

        send_img_message(sender_id, url_msg)
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2 for pick')

    def on_enter_state3(self, event):
        print("I'm entering state3 for sing1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "一起喵喵喵喵喵")

    def on_exit_state3(self, event):
        print('Leaving state3 for sing1')
        
    def on_enter_state4(self, event):
        print("I'm entering state4 for sing2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "哎唷喵喵喵喵喵")

    def on_exit_state4(self, event):
        print('Leaving state4 for sing2')

    def on_enter_state5(self, event):
        print("I'm entering state5 for sing3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "迷戀上你的壞笑")

    def on_exit_state5(self, event):
        print('Leaving state5 for sing3')

    def on_enter_state6(self, event):
        print("I'm entering state6 for sing4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "接\n龍\n大\n成\n功\n")
        self.go_back()

    def on_exit_state6(self):
        print('Leaving state6 for sing4')

    def on_enter_state7(self, event):
        print("I'm entering state7 for pick a girl")

        sender_id = event['sender']['id']
        with open('data.json') as f:
            url_pick = json.load(f)

        pick_num = len(url_pick) - 1
        rand_num = randint(0, pick_num)
        send_img_message(sender_id, url_pick[rand_num])
        self.go_back()

    def on_exit_state7(self):
        print('Leaving state7 for pick a girl')

    def on_enter_state8(self, event):
        print("I'm entering state8 for buttons")

        sender_id = event['sender']['id']
        
        buttons = [{
            'type': 'postback',
            'title': "Python",
            'payload': 'Python'
        },{
            'type': 'postback',
            'title': "Java",
            'payload': 'Java'
        },{
            'type': 'postback',
            'title': "C++",
            'payload': 'C++'
        }]
        
        send_button_message(sender_id, "我是用什麼語言寫的？", buttons)

    def on_exit_state8(self, event):
        print("Leaving state8")

    def on_enter_state9(self, event):
        print("I'm entering state9")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "答對了呢嘻嘻")
        self.go_back()

    def on_exit_state9(self):
        print("Leaving state9")

    def on_enter_state10(self, event):
        print("I'm entering state9")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "猜錯了嘻嘻")
        self.go_back()

    def on_exit_state10(self):
        print("Leaving state10")

    def on_enter_state11(self, event):
        print("I'm entering state11")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "猜錯了唷嘻嘻")
        self.go_back()

    def on_exit_state11(self):
        print("Leaving state11")

    def on_enter_state12(self, event):
        print("I'm entering state12")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "唱錯了啦><\n是在你面前撒個嬌啦")
        self.go_back()

    def on_exit_state12(self):
        print("Leaving state12")

    def on_enter_state13(self, event):
        print("I'm entering state13")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "唱錯了啦><\n是我的心臟蹦蹦跳啦")
        self.go_back()

    def on_exit_state13(self):
        print("Leaving state13")

    def on_enter_state14(self, event):
        print("I'm entering state14")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "唱錯了啦><\n是你不說愛我我就喵喵喵啦")
        self.go_back()

    def on_exit_state14(self):
        print("Leaving state14")
