from datetime import datetime
class Spy:
    def __init__(self, name, age, rating):
        self.name=name
        self.age=age
        self.rating=rating
        self.is_online=True
        self.chats = []
        self.status_message = None

class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy=Spy('isha', '21','8.8')

friend_one = Spy('Ravi', 9.9, 27)
friend_two = Spy('Mahesh', 4.39, 21)
friend_three = Spy('lovely', 6.95, 37)


friends = [friend_one, friend_two, friend_three]
