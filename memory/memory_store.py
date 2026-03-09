conversation_memory = []


def save_to_memory(user_input, response):

    conversation_memory.append({
        "user": user_input,
        "response": response
    })


def get_memory():

    return conversation_memory