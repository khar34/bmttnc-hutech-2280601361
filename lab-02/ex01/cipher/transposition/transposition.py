import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        rows = math.ceil(len(text) / key)
        grid = [''] * rows
        for i in range(len(text)):
            row = i // key
            grid[row] += text[i]
        for col in range(key):
            for row in range(rows):
                if col < len(grid[row]):
                    encrypted_text += grid[row][col]
        return encrypted_text

    def decrypt(self, text, key):
        rows = math.ceil(len(text) / key)
        num_full_cols = len(text) % key if len(text) % key != 0 else key
        grid = [''] * key
        pos = 0
        for col in range(key):
            num_rows = rows if col < num_full_cols else rows - 1
            for _ in range(num_rows):
                if pos < len(text):
                    grid[col] += text[pos]
                    pos += 1
        decrypted_text = ''
        for row in range(rows):
            for col in range(key):
                if row < len(grid[col]):
                    decrypted_text += grid[col][row]
        return decrypted_text
