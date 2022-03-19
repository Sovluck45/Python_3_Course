import json
import logging
import sys
import logs.client_log_config
from socket import socket, AF_INET, SOCK_STREAM
from server_content.variables import default_port, default_ip_address
from server_content.functions import get_message, send_message, jim_presence, check_response

client_logger = logging.getLogger("client")


def connect_func():
    client_logger.info(f"Происходит соединение с сервером {default_port}")
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            client_logger.critical(f"Указан неподходящий порт для запуска сервера")
    except IndexError:
        client_logger.debug("Установлены значения адреса и порта по умолчанию")
        server_address = default_ip_address
        server_port = default_port
    except ValueError:
        client_logger.error("В качестве порта может быть указано только число в диапазоне от 1024 до 65535")
        sys.exit(1)

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    message_to_server = jim_presence()
    send_message(client_socket, message_to_server)
    try:
        answer = check_response(get_message(client_socket))
        client_logger.debug(f"Ответ сервера: {answer}")
    except (ValueError, json.JSONDecodeError):
        client_logger.error("Не удалось декодировать сообщение от сервера!")


if __name__ == "__main__":
    connect_func()
