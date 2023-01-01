from chatgpt.api import ChatGPT

# TODO: HANDLE chatgpt.exceptions.StatusCodeException: <Response [429 Too Many Requests]>


def sendRequest(session_token, message):
    chat = ChatGPT(
        session_token=session_token,
        user_agent="Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    )
    chat.authenticate()
    response = chat.send_message(message)
    chat.close()
    print(response.content)
    return response.content
