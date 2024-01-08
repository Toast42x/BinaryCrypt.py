def xor_decode(encoded_text, key):

    binary_encoded_text = encoded_text
    binary_key = ''.join(format(ord(char), '08b') for char in key)

    repeated_key = (binary_key * (len(binary_encoded_text) // len(binary_key) + 1))[:len(binary_encoded_text)]

    decoded_text = ''.join(str(int(bit_encoded) ^ int(bit_key)) for bit_encoded, bit_key in zip(binary_encoded_text, repeated_key))

    decoded_text = ''.join(chr(int(decoded_text[i:i+8], 2)) for i in range(0, len(decoded_text), 8))

    return decoded_text

encoded_message = "0011101100000000000011110001111000001010010110000100101100111101001101100010000101000101001001100001110000000110000110110000111100001100000101110001010001000100"

decoded_message = xor_decode(encoded_message, "secretkey")

print(f"Encoded Message : {encoded_message}")
print(f"Decoded Message : {decoded_message}")