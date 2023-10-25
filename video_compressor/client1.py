import socket
import struct

class ChatClient:
    def __init__(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = "0.0.0.0"
        self.tcp_port = 9000
        self.udp_port = 9001
        self.token = None

    def create_room(self, server_addr, room_name):
        header = struct.pack('!B B B 29s', len(room_name), 1, 0, b'')
        self.tcp_socket.connect(server_addr)
        self.tcp_socket.send(header + room_name.encode('utf-8'))
        self.token = self.tcp_socket.recv(255).decode('utf-8')
        self.tcp_socket.close()

    def join_room(self, server_addr, room_name):
        header = struct.pack('!B B B 29s', len(room_name), 2, 0, b'')
        self.tcp_socket.connect(server_addr)
        self.tcp_socket.send(header + room_name.encode('utf-8'))
        self.token = self.tcp_socket.recv(255).decode('utf-8')
        self.tcp_socket.close()

    def send_message(self, server_addr, room_name, message):
        header = struct.pack('!B B', len(room_name), len(self.token))
        self.udp_socket.sendto(header + room_name.encode('utf-8') + self.token.encode('utf-8') + message.encode('utf-8'), server_addr)

    def receive_messages(self):
        while True:
            data, _ = self.udp_socket.recvfrom(4094)
            print(f"Received: {data.decode('utf-8')}")


    def start(self):
        # UDPソケットをアドレスとポート番号にバインド
        self.udp_socket.bind((self.host, self.udp_port))

        # TCPソケットをアドレスとポート番号にバインド
        self.tcp_socket.bind((self.host, self.tcp_port))



if __name__ == '__main__':
    client = ChatClient()
    client.start()
    client.create_room(('0.0.0.0', 9000), 'test_room')
    client.send_message(('0.0.0.0', 9000), 'test_room', 'Hello, World!')
    client.receive_messages()