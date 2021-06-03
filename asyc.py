import socket
from select import select

tasks = []
to_read = {}
to_write = {}


def server():
    server_sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 9000))
    server_sock.listen()

    while True:
        yield ('read', server_sock)

        client_socket, addr = server_sock.accept()
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield ('read', client_socket)
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello world suchka /n'.encode()
            yield ('write', client_socket)
            client_socket.send(response)

    client_socket.close()


def event_loop():
    while any([to_read, to_write, tasks]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop()
            status, sock = next(task)


            if status == 'read':
                to_read[sock] = sock
            elif status == 'write':
                to_write[sock] = sock
        except StopIteration:
            pass


tasks.append(server())
event_loop()
