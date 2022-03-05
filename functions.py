import json
from server_content.variables import package_length, encoding


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
