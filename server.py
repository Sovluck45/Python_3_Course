import json
import sys
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from server_content.variables import default_port, connections
from server_content.functions import get_message, send_message, client_message


def connect_func():
    try:
        if "-p" in sys.argv:
            listen_port = int(sys.argv[sys.argv.index("-p") + 1])
        else:
            listen_port = default_port
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print("После параметра -p необходимо указать номер порта")
        sys.exit(1)
    except ValueError:
        print("В качастве порта может быть указано только число в диапазоне от 1024 до 65535")
        sys.exit(1)

    try:
        if "-a" in sys.argv:
            listen_address = sys.argv[sys.argv.index("-a") + 1]
        else:
            listen_address = ""
    except IndexError:
        print("После параметра -a необходимо указать адрес, который будет слушать сервер")
        sys.exit(1)

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind((listen_address, listen_port))
    server_socket.listen(connections)

    while True:
        client, client_address = server_socket.accept()
        try:
            client_msg = get_message(client)
            print(f"Сообщение от клиента:\n{client_msg}")
            response_to_client = client_message(client_msg)
            send_message(client, response_to_client)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print("Не удалось декодировать сообщение клиента!")
            client.close()


if __name__ == "__main__":
    connect_func()
