from datetime import datetime

class User:
    def __init__(self, userName):
        self.userName = userName


class Message:
    def __init__(self, sender, content, system=False):
        self.sender = sender
        self.content = content
        self.time = datetime.now()
        self.system = system   # flag for system messages


class ChatRoom:
    def __init__(self, roomName):
        self.roomName = roomName
        self.users = []
        self.messages = []

    # -------- USER MANAGEMENT --------
    def addUser(self, user):
        # prevent duplicate usernames
        for u in self.users:
            if u.userName == user.userName:
                print("Username already exists!")
                return

        self.users.append(user)
        join_msg = Message(user, f"{user.userName} joined the chat.", system=True)
        self.addMessage(join_msg)
        print(f"{user.userName} added successfully.")

    def removeUser(self, userName):
        for user in self.users:
            if user.userName == userName:
                self.users.remove(user)
                leave_msg = Message(user, f"{userName} left the chat.", system=True)
                self.addMessage(leave_msg)
                print(f"{userName} removed from chat.")
                return
        print("User not found!")

    def showUsers(self):
        print("\nActive Users:")
        if not self.users:
            print("No users in chat.")
        for user in self.users:
            print(f"- {user.userName}")
        print()

    # -------- MESSAGE MANAGEMENT --------
    def addMessage(self, message):
        self.messages.append(message)

    def showHistory(self):
        print("\n----- Chat History -----\n")

        if not self.messages:
            print("No messages yet!")

        for msg in self.messages:
            time_str = msg.time.strftime("%H:%M:%S")

            if msg.system:
                print(f"[{time_str}] *** {msg.content}")
            else:
                print(f"[{time_str}] {msg.sender.userName}: {msg.content}")

        print("\n------------------------\n")

    # -------- CHAT SYSTEM --------
    def startChat(self):
        if len(self.users) < 2:
            print("Need at least 2 users to start chat!")
            return

        print("\n-----------------------------------------")
        print("Chat Started")
        print("Commands:")
        print("0                -> Exit chat")
        print("/add username    -> Add user")
        print("/leave username  -> Remove user")
        print("/users           -> Show active users")
        print("-----------------------------------------\n")

        turn = 0

        while True:
            if len(self.users) < 1:
                print("No users left. Chat ended.")
                break

            current_user = self.users[turn % len(self.users)]
            msg = input(f"{current_user.userName}: ")

            # EXIT CHAT
            if msg == "0":
                print("\n--------")
                print("Chat End")
                print("--------\n")
                break

            # ADD USER
            elif msg.startswith("/add"):
                parts = msg.split()
                if len(parts) == 2:
                    self.addUser(User(parts[1]))
                else:
                    print("Usage: /add username")
                continue

            # REMOVE USER
            elif msg.startswith("/leave"):
                parts = msg.split()
                if len(parts) == 2:
                    self.removeUser(parts[1])
                    turn = 0
                else:
                    print("Usage: /leave username")
                continue

            # SHOW USERS
            elif msg == "/users":
                self.showUsers()
                continue

            # NORMAL MESSAGE
            message = Message(current_user, msg)
            self.addMessage(message)

            turn += 1


# --------------- MAIN PROGRAM -------------------
def main():
    print("\n----------------------")
    roomName = input("Chat Room Name: ")
    chatRoom = ChatRoom(roomName)

    # initial users
    sender1 = input("User 1: ")
    sender2 = input("User 2: ")

    chatRoom.addUser(User(sender1))
    chatRoom.addUser(User(sender2))

    while True:
        print("-------------")
        print("Program Menu")
        print("-------------\n")

        print("1. Start Chat")
        print("2. Show Chat History")
        print("3. Add User")
        print("4. Remove User")
        print("5. Show Active Users")
        print("0. Exit Program")

        try:
            n = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if n == 1:
            chatRoom.startChat()

        elif n == 2:
            chatRoom.showHistory()

        elif n == 3:
            new_user = input("Enter username: ")
            chatRoom.addUser(User(new_user))

        elif n == 4:
            rem_user = input("Enter username to remove: ")
            chatRoom.removeUser(rem_user)

        elif n == 5:
            chatRoom.showUsers()

        elif n == 0:
            print("\n------------")
            print("Program End")
            print("------------")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()