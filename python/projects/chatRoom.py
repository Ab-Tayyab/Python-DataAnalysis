from datetime import datetime
class User:
    def __init__(self, userName):
        self.userName = userName


class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.time=datetime.now()

class ChatRoom:
    def __init__(self, roomName):
        self.roomName = roomName
        self.users = []
        self.messages = []

    def addUser(self, user):
        if len(self.users) < 2:
            self.users.append(user)

    def addMessage(self, message):
        self.messages.append(message)

    def showHistory(self):
        print("\n-----Chat History-----\n")
        if not self.messages:
            print("No Message yet!")

        for msg in self.messages:
            time_str = msg.time.strftime("%H:%M:%S")
            print(f"[{time_str}]=> {msg.sender.userName}: {msg.content}")
        print("\n----------------------\n")
    def startChat(self):
        if len(self.users) < 2:
            print("Need 2 user to start chat!")
            return
        
        print("\n-----------------------------------------")
        print("Chat Started")
        print("Press 0 for exit chat and return to menu:")
        print("-----------------------------------------\n")

        turn = 0
        while True:
            current_user = self.users[turn]
            msg = input(f"{current_user.userName}: ")
            if msg == "0":
                print("\n--------")
                print("Chat End")
                print("--------\n")
                break
            message = Message(current_user, msg)
            self.addMessage(message)
            turn = 1 - turn


# --------------- Main Program-------------------
def main():
    print("\n----------------------")
    roomName = input("Chat Room Name: ")
    chatRoom = ChatRoom(roomName)

    sender1 = input("User 1: ")
    sender2 = input("User 2: ")
    print("----------------------\n")
    createUser1 = User(sender1)
    createUser2 = User(sender2)

    chatRoom.addUser(createUser1)
    chatRoom.addUser(createUser2)

    while True:
        print("-------------")
        print("Programm Menu")
        print("-------------\n")
    
        print("1. Start Chat")
        print("2. Show Chat History")
        print("0. Exit Program")

        n = int(input("Enter Choice: "))

        if n == 1:
            chatRoom.startChat()
        elif n == 2:
            chatRoom.showHistory()
        elif n == 0:
            print("\n------------")
            print("Programm end")
            print("------------")

            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()