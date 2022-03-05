import json
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from server_content.variables import action, account_name, response, presence, msg_time, user, \
    error, default_port, default_ip_address
from server_content.functions import get_message, send_message


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


def connect_func():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = default_ip_address
        server_port = default_port
    except ValueError:
        print("В качестве порта может быть указано только число в диапазоне от 1024 до 65535")
        sys.exit(1)

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    message_to_server = jim_presence()
    send_message(client_socket, message_to_server)
    try:
        answer = check_response(get_message(client_socket))
        print(f"Ответ сервера: {answer}")
    except (ValueError, json.JSONDecodeError):
        print("Не удалось декодировать сообщение от сервера!")


if __name__ == "__main__":
    connect_func()
