import asyncio

class ChatRoom:
    def __init__(self):
        self.clients = {}

    def create_chat_root(title, max_clients):
        title = input("Enter your name: ")
        return title


class ChatClient:
    def __init__(self):
        self.server_ip = '0.0.0.0'
        self.tcp_port = 9000
        self.udp_port = 9001
        self.tcp_socket = None
        self.udp_socket = None
        self.chat_root = ChatRoom()

    def create_client(self):
        name = input("Enter your name: ")
        if not isinstance(name, str):
            raise ValueError("文字列を入力してください")
        return name


    async def join_room(self, roomname):
        reader, writer = await asyncio.open_connection(self.server_ip, self.tcp_port)
        join_message = f"{roomname}:join"
        writer.write(join_message.encode())
        await writer.drain()
        writer.close()

    async def send_message(self, roomname, message):
        self.udp_socket = await asyncio.get_event_loop().create_datagram_endpoint(lambda: None, remote_addr=(self.server_ip, self.udp_port))
        message_size = len(message)
        send_message = f"{roomname}:{message_size}:{message}"
        self.udp_socket[1].sendto(send_message.encode(), (self.server_ip, self.udp_port))

    def start(self):
        # name = self.create_client()
        # self.chat_root.create_chat_root()

        asyncio.get_event_loop().run_until_complete(self.join_room('room1'))
        asyncio.get_event_loop().run_until_complete(self.send_message('room1', 'Hello, World!'))

if __name__ == "__main__":
    client = ChatClient()
    client.start()