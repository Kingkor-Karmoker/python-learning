# code for problem 8.11:
# starting from 8.10:
def show_messages(messages):
    for message in messages:
        print(message)
print('\n')

messages = ["Life is not easy", "Dont believe anyone 100%", "Win yourself first before winning others"]
show_messages(messages)

messages_sent =[]
print('\n')
def send_messages(messages_to_sent):
    while messages_to_sent:
        msg = messages_to_sent.pop(0)
        print(f"sending msg: {msg}")
        messages_sent.append(msg)

send_messages(messages[:])
print(f"\nnew sent messages list: {messages_sent}")
print(f"Original list: {messages}")
