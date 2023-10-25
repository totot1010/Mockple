import socket
import struct
import threading

class ChatServer:
    def __init__(self):
        self.rooms = {}
        self.tokens = {}
        self.host = "0.0.0.0"
        self.tcp_port = 9000
        self.udp_port = 9001
        self.max_listen_num = 5
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        
        # クライアントからの接続の受け入れて処理
        self.accept_and_handle_client()




        
        while True:
            client_socket, addr = self.tcp_socket.accept()
            header = client_socket.recv(32)
            room_name_size, operation, state, operation_payload_size = struct.unpack('!B B B 29s', header)
            room_name = client_socket.recv(room_name_size).decode('utf-8')
            
            if operation == 1:  # Create room
                # Generate token and store
                token = "SOME_RANDOM_TOKEN"
                self.tokens[token] = room_name
                self.rooms[room_name] = []
                client_socket.send(token.encode())
            elif operation == 2:  # Join room
                # Generate token and store
                token = "SOME_OTHER_RANDOM_TOKEN"
                self.tokens[token] = room_name
                self.rooms[room_name].append(addr)
                client_socket.send(token.encode())
            
            client_socket.close()


    def accept_and_handle_client(self):
        """クライアントからの接続の受け入れて処理"""
        # TCPソケットをアドレスとポート番号にバインド
        self.tcp_socket.bind((self.host, self.tcp_port))
        # クライアントからの接続待ち
        self.tcp_socket.listen(self.max_listen_num)

        print(f"TCP Server started at {self.host}:{self.tcp_port}")

        while True:
            # クライアントからの接続受付
            client_socket, addr = self.tcp_socket.accept()
            # クライアント接続ごとに新しいスレッドが作成
            threading.Thread(target=self.handle_tcp, args=(client_socket, addr)).start()


    def handle_tcp(self, client_socket, addr):
        """クライアントからのTCP接続を処理

        Args:
            client_socketはクライアントからの接続（ソケットオブジェクト）を、
            addrはクライアントのアドレス情報を参照


        """

        header = self.tcp_socket.recv(32)
        room_name_size, operation, state, operation_payload_size = struct.unpack('!B B B 29s', header)
        room_name = self.tcp_socket.recv(room_name_size).decode('utf-8')
        
        if operation == 1:  # Create room
            # Generate token and store
            token = "SOME_RANDOM_TOKEN"
            self.tokens[token] = room_name
            self.rooms[room_name] = []
            self.tcp_socket.send(token.encode())
        elif operation == 2:  # Join room
            # Generate token and store
            token = "SOME_OTHER_RANDOM_TOKEN"
            self.tokens[token] = room_name
            self.rooms[room_name].append(addr)
            self.tcp_socket.send(token.encode())
        
        self.tcp_socket.close()




    def handle_udp(self):
        while True:
            data, addr = self.udp_socket.recvfrom(4096)
            room_name_size, token_size = struct.unpack('!B B', data[:2])
            room_name = data[2:2+room_name_size].decode('utf-8')
            token = data[2+room_name_size:2+room_name_size+token_size].decode('utf-8')
            
            if self.tokens.get(token) == room_name:
                for client in self.rooms[room_name]:
                    self.udp_socket.sendto(data[2+room_name_size+token_size:], client)

if __name__ == '__main__':
    server = ChatServer()
    server.start()
