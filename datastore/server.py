import os
import selectors
import socket
import types

from controller import parse_input
from logzero import logger


def accept_wrapper(sock: socket.socket) -> None:
    """Set up the listening socket in non-blocking mode.

    :type sock: socket.socket
    """
    conn, addr = sock.accept()
    ip, port = addr
    logger.warn(f'Accepted connection from {ip}:{port}')
    conn.setblocking(False)

    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE

    sel.register(conn, events, data=data)


def service_connection(key: selectors.SelectorKey, mask: int) -> None:
    """Handle client conneciton.

    :type key: selectors.SelectorKey
    :type mask: int
    """
    sock = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            logger.warn(f'Closing connection to {data.addr}')
            sel.unregister(sock)
            sock.close()

    if mask & selectors.EVENT_WRITE:
        if data.outb:
            data.outb = str.encode(str(parse_input(data.outb)))
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


def start_server():
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        lsock.bind((HOST, PORT))
    except Exception as exc:
        logger.error(exc)
        os._exit(1)

    lsock.listen()

    logger.warn(f'Listening on {HOST}:{PORT}')

    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, data=None)

    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    accept_wrapper(key.fileobj)
                else:
                    service_connection(key, mask)
    except KeyboardInterrupt:
        logger.error('Caught keyboard interrupt, exiting')
    finally:
        sel.close()


sel = selectors.DefaultSelector()

HOST = '127.0.0.1'
PORT = 65432
