def show_messages(messages):
    """Print all messages in the list"""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_item = messages.pop()
        print(f'Printing: {current_item}')
        sent_messages.append(current_item)

msgs = ["hello there", "how are u?", ":)"]

sent_msgs = []
send_messages(msgs[:], sent_msgs)

print(msgs, sent_msgs)


# def show_messages(messages):
#     """Print all mesages in the list."""
#     for message in messages:
#         print(message)

# def send_messages(messages, sent_messages):
#     for i in range(len(messages)):
#         current = messages[0]
#         print(f'Printing: {current}')
#         messages.pop(0)
#         sent_messages.append(current)

# msgs = ['hola', 'como', 'estas', 'me', 'llamo', 'aaron']
# sent_msgs = []
# send_messages(msgs, sent_msgs)
# print(msgs, sent_msgs)






