class HuffmanNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def decode_huffman(root, encoded_data):
    decoded_data = ""
    current = root

    for bit in encoded_data:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.left is None and current.right is None:
            decoded_data += current.data
            current = root

    return decoded_data

# Example usage:
# Construct a sample Huffman tree
root = HuffmanNode(None)
root.left = HuffmanNode(None)
root.right = HuffmanNode('A')
root.left.left = HuffmanNode('B')
root.left.right = HuffmanNode('C')

# Encoded data (e.g., "1001011")
encoded_data = "1001011"

# Decode the encoded data using the Huffman tree
decoded_data = decode_huffman(root, encoded_data)

print("Decoded Data:", decoded_data)  # Output: "ABC"
