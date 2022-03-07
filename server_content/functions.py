import json
import time

from server_content.variables import action, account_name, response, connections, presence, msg_time, user, \
    error, default_port, response_ip_address, package_length, encoding


def get_message(client):
    encoded_response = client.recv(package_length)
    if isinstance(encoded_response, bytes):
        response = json.loads(encoded_response.decode(encoding))
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    if not isinstance(message, dict):
        raise TypeError
    sock.send(json.dumps(message).encode(encoding))


def client_message(message):
    if action in message and message[action] == presence and msg_time in message \
            and user in message and message[user][account_name] == "User":
        return {response: 200}
    return {response_ip_address: 400, error: "Ошибка отправки сообщения"}


def jim_presence(acc_name="User"):
    msg = \
        {
            action: presence,
            msg_time: time.time(),
            user: {account_name: acc_name}
        }
    return msg


def check_response(message):
    if response in message:
        if message[response] == 200:
            return "200: OK"
        return f"400: {message[error]}"
    raise ValueError
