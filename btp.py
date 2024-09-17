import numpy as np
import random


class Server:
    def __init__(self):
        self.user_ciphers = dict()

    def enroll(self, user, cipher):
        self.user_ciphers[user] = np.array(cipher)

    def authenticate(self, user, query_cipher, threshold=0.5):
        if user in self.user_ciphers:
            stored_cipher = self.user_ciphers[user]
            hamming_distance = sum(xor(stored_cipher, query_cipher)) / len(stored_cipher)
            return hamming_distance < threshold
        else:
            return False


class Client:
    def __init__(self, user):
        self.user = user
        self.secret_key = None

    def enroll(self, bit_vector, server):
        self.secret_key = generate_random_bits(len(bit_vector))
        cipher = xor(bit_vector, self.secret_key)
        server.enroll(self.user, cipher)
        print("Enrollment successful.")

    def authenticate(self, bit_vector, server):
        if self.secret_key is not None:
            cipher = xor(bit_vector, self.secret_key)
            auth = server.authenticate(self.user, cipher)
            if auth:
                print("Authentication Success.")
            else:
                print("Authentication Failed.")
            return auth
        else:
            raise Exception("User not enrolled!")


def generate_random_bits(num_bits):
    return np.random.randint(0, 2, num_bits)


def xor(vec1, vec2):
    return np.bitwise_xor(vec1, vec2)


if __name__ == "__main__":
    server = Server()
    client = Client('user1')

    print('-------- ENROLL --------')
    vector1 = np.array([1, 1, 0, 0, 1])
    client.enroll(vector1, server)

    print('\n-------- AUTHENTICATE (Genuine) --------')
    vector2 = np.array([1, 1, 1, 0, 1])  # Only 1 bit off, it should authenticate
    client.authenticate(vector2, server)

    print('\n-------- AUTHENTICATE (Imposter) --------')
    vector3 = np.array([0, 0, 1, 1, 1])  # Several bits off, should NOT authenticate
    client.authenticate(vector3, server)



