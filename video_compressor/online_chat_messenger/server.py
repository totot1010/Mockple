import asyncio

class ChatRoom:
    def __init__(self, title, max_clients):
        self.title = title
        self.max_clients = max_clients
        self.clients = {}

class ChatClient:
    def __init__(self, address, port, extra_data=None):
        self.address = address
        self.port = port
        self.extra_data = extra_data

class ChatServer:
    def __init__(self):
        self.chat_rooms = {}
        self.tcp_port = 9000
        self.udp_port = 9001

    async def handle_tcp(self, reader, writer):
        data = await reader.read(100)
        message = data.decode()
        # Handle TCP Connections for creating new rooms here

    async def handle_udp(self):
        # Handle UDP Connections for chat messages here
        pass

    async def tcp_server(self):
        server = await asyncio.start_server(self.handle_tcp, '127.0.0.1', self.tcp_port)
        async with server:
            await server.serve_forever()

    async def udp_server(self):
        transport, protocol = await asyncio.get_event_loop().create_datagram_endpoint(lambda: self.handle_udp, local_addr=('127.0.0.1', self.udp_port))
        await protocol.wait_closed()

    def start(self):
        asyncio.get_event_loop().run_until_complete(asyncio.gather(self.tcp_server(), self.udp_server()))

if __name__ == "__main__":
    server = ChatServer()
    server.start()