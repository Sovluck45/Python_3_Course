import json
import logging
import sys
import logs.server_log_config
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from server_content.variables import default_port, connections
from server_content.functions import get_message, send_message, client_message

server_logger = logging.getLogger("server")


def connect_func():
    server_logger.debug(f"Происходит соединение с портом {default_port}")
    try:
        if "-p" in sys.argv:
            listen_port = int(sys.argv[sys.argv.index("-p") + 1])
        else:
            listen_port = default_port
        if listen_port < 1024 or listen_port > 65535:
            server_logger.critical(f"Указан неподходящий порт для запуска сервера")
    except IndexError:
        server_logger.error("После параметра -p необходимо указать номер порта")
        sys.exit(1)
    except ValueError:
        server_logger.error("В качастве порта может быть указано только число в диапазоне от 1024 до 65535")
        sys.exit(1)
    server_logger.debug("Происходит соединение с адресом клиента")
    try:
        if "-a" in sys.argv:
            listen_address = sys.argv[sys.argv.index("-a") + 1]
        else:
            listen_address = ""
    except IndexError:
        server_logger.error("После параметра -a необходимо указать адрес, который будет слушать сервер")
        sys.exit(1)

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind((listen_address, listen_port))
    server_socket.listen(connections)

    while True:
        client, client_address = server_socket.accept()
        server_logger.info(f"Установлено соединение с клиентом: {client_address}")
        try:
            client_msg = get_message(client)
            server_logger.debug(f"Сообщение от клиента:\n{client_msg}")
            response_to_client = client_message(client_msg)
            send_message(client, response_to_client)
            server_logger.info(f"Клиенту отправлено сообщение {response_to_client}")
            server_logger.debug(f"Соединение с клиентом {client_address} заканчивается")
            client.close()
        except (ValueError, json.JSONDecodeError):
            server_logger.error("Не удалось декодировать сообщение клиента!")
            client.close()


if __name__ == "__main__":
    connect_func()
