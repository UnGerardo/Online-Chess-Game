import socket


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'IP ADDRESS'
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id = self.connect()

    def connect(self):
        # connect to server
        self.client.connect(self.addr)
        # receive data from server and store in self.id - loop not needed because data is small
        return self.client.recv(2048).decode()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            # send data to server
            self.client.send(str.encode(data))
            # receive data from server - need loop to get entirety of data (too big)
            datas = b''
            while True:
                chunk = self.client.recv(2048)
                datas += chunk
                if len(chunk) < 2048:
                    # either 0 or end of data
                    break
            reply = datas.decode()
            # return reply to store in gameState with send_data func in main.py
            return reply
        except socket.error as e:
            return str(e)
