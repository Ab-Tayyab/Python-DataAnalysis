#  Create a Chat System using Object-Oriented Programming (OOP) concepts.
# You need to create the following classes:
# • User
# • Message
# • ChatRoom
#  The system should implement the following functionalities:
# • Sending messages
# • Viewing chat history
# • User joining and leaving the chat room

from datetime import datetime

class User:
    def __init__(self,userName):
        self.userName = userName


class Message:
    def __init__(self,sender,content):
        self.sender = sender
        self.content=content

class ChatRoom:
    def __init__(self,roomName):
        self.roomName = roomName
        self.users = []
        self.messages=[]
    def addUser(self,user):
        if len(self.users)<2:
            self.users.append(user)



def main():
    roomName = input("Enter chat room name: ")
    chatRoom = ChatRoom(roomName)

    sender1 = input("Enter name of user 1: ")
    sender2 = input("Enter name of user 2: ")
    createUser1 = User(sender1)
    createUser2 = User(sender2)

    chatRoom.addUser(createUser1)
    chatRoom.addUser(createUser2)

    while True:
        print("-------Menu-------")
        print("1. Start Chat")
        print("2. Show Chat History")
        print("0. Exit Program")

        n = int(input("Enter Choice: "))

        if(n==1):
            print("Start Chat")
        elif n==2:
            print("Chat history")
        elif n==0:
            print("Programm end")
            break
        else:
            print("Invalid Choice")
if __name__ == "__main__":
    main()