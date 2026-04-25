class User:
    def __init__(self, name):
        self.name = name


class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content


class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def add_user(self, user):
        if len(self.users) < 2:
            self.users.append(user)

    def add_message(self, message):
        self.messages.append(message)

    def show_history(self):
        print("\n--- Chat History ---")
        if not self.messages:
            print("No messages yet.")
        for msg in self.messages:
            print(f"{msg.sender.name}: {msg.content}")
        print("--------------------\n")

    def start_chat(self):
        if len(self.users) < 2:
            print("Need 2 users to start chat.")
            return

        print("\n--- Chat Started ---")
        print("Press 0 to exit chat and return to menu.\n")

        turn = 0  # 0 = user1, 1 = user2

        while True:
            current_user = self.users[turn]

            msg = input(f"{current_user.name}: ")

            if msg == "0":
                print("Exiting chat...\n")
                break

            message = Message(current_user, msg)
            self.add_message(message)

            # switch user
            turn = 1 - turn


# ---------------- MAIN PROGRAM ----------------

def main():
    room_name = input("Enter chat room name: ")
    chatroom = ChatRoom(room_name)

    user1_name = input("Enter first sender name: ")
    user2_name = input("Enter second sender name: ")

    user1 = User(user1_name)
    user2 = User(user2_name)

    chatroom.add_user(user1)
    chatroom.add_user(user2)

    while True:
        print("\n===== MENU =====")
        print("1. Start Chat")
        print("2. Show Chat History")
        print("0. Exit Program")

        choice = input("Choose option: ")

        if choice == "1":
            chatroom.start_chat()

        elif choice == "2":
            chatroom.show_history()

        elif choice == "0":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()