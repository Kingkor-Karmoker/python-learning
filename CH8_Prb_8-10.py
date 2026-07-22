# code for problem 8.10:
# copied code from 8.9:
def show_messages(messages):
    for message in messages:
        print(message)
        print('\n')

messages = ["Life is not easy", "Dont believe anyone 100%", "Win yourself first before winning others"]
show_messages(messages)
#8.10 code starts here:
messages_sent =[]
def sent_messages(messages_to_sent):
    while messages_to_sent:
        msg = messages_to_sent.pop(0)
        print(f"sending msg: {msg}")
        messages_sent.append(msg)

sent_messages(messages)
print(messages)
print(messages_sent)