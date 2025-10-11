

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = [] 

    def call(self, other_phone):
        call_info = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_info)
        self.call_history.append(call_info)

    def show_call_history(self):
        print(f"\nCall history for {self.phone_number}:")
        for call in self.call_history:
            print(call)

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)  
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: '{content}'")

    
    def show_outgoing_messages(self):
        print(f"\nOutgoing messages from {self.phone_number}:")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(f"To {msg['to']}: '{msg['content']}'")

    def show_incoming_messages(self):
        print(f"\nIncoming messages to {self.phone_number}:")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(f"From {msg['from']}: '{msg['content']}'")

    def show_messages_from(self, other_phone):
        print(f"\nMessages from {other_phone.phone_number} to {self.phone_number}:")
        for msg in self.messages:
            if msg["from"] == other_phone.phone_number and msg["to"] == self.phone_number:
                print(f"'{msg['content']}'")


# phone1 = Phone("065098767")
# phone2 = Phone("098789879")

# phone1.call(phone2)
# phone2.send_message(phone1, "cc cv ?")
# phone1.send_message(phone2, "oui, merci")

# phone1.show_call_history()
# phone2.show_call_history()


# phone1.show_outgoing_messages()
# phone1.show_incoming_messages()

# phone1.show_messages_from(phone2)
