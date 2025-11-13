import heapq
from collections import Counter, namedtuple

# Node structure for the Huffman tree
class Node:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    # required for heapq to compare nodes with same frequencies
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency):
    """
    Build Huffman tree using a min-heap (greedy merges of two smallest freq nodes).
    frequency: dictionary mapping symbol -> frequency
    Returns the root node of the Huffman tree.
    """
    heap = []
    # push leaf nodes
    for sym, fr in frequency.items():
        heapq.heappush(heap, Node(fr, symbol=sym))

    # Edge case: empty input
    if not heap:
        return None

    # Edge case: single unique symbol -> create a dummy partner so tree has depth
    if len(heap) == 1:
        only = heapq.heappop(heap)
        # create a dummy node with zero freq to allow generating a '0' code
        parent = Node(only.freq, left=only, right=Node(0, symbol=None))
        return parent

    # Greedy step: keep combining two smallest nodes
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(root):
    """
    Traverse the Huffman tree and generate codes (symbol -> bitstring).
    """
    codes = {}
    def _gen(node, prefix):
        if node is None:
            return
        if node.symbol is not None:
            # leaf node
            codes[node.symbol] = prefix or "0"  # if prefix empty (single symbol), assign "0"
        else:
            _gen(node.left, prefix + "0")
            _gen(node.right, prefix + "1")
    _gen(root, "")
    return codes

def huffman_encode(text):
    """
    Encode input text using Huffman coding.
    Returns (encoded_bitstring, codes, tree_root).
    """
    if text == "":
        return "", {}, None

    freq = Counter(text)
    root = build_huffman_tree(freq)
    codes = generate_codes(root)
    encoded = "".join(codes[ch] for ch in text)
    return encoded, codes, root

def huffman_decode(bitstring, root):
    """
    Decode a bitstring using the Huffman tree root.
    """
    if root is None:
        return ""
    # if the tree has only one symbol, that symbol code is '0' repeated
    if root.left is not None and root.right is not None:
        res_chars = []
        node = root
        for bit in bitstring:
            node = node.left if bit == "0" else node.right
            if node.symbol is not None:
                res_chars.append(node.symbol)
                node = root
        return "".join(res_chars)
    else:
        # Single-symbol case: bitstring length indicates count of the only symbol
        # find the symbol
        # traverse until leaf
        node = root
        while node.symbol is None:
            node = node.left or node.right
        return node.symbol * len(bitstring)

# Example usage
if __name__ == "__main__":
    sample = "this is an example for huffman encoding"
    encoded, codes, tree = huffman_encode(sample)
    decoded = huffman_decode(encoded, tree)

    print("Original:", sample)
    print("Frequencies:", dict(Counter(sample)))
    print("\nCodes:")
    for sym, code in sorted(codes.items(), key=lambda x: (len(x[1]), x[0])):
        # show readable representation for whitespace
        display_sym = repr(sym) if sym.isspace() else sym
        print(f" {display_sym!s:4} -> {code}")

    print("\nEncoded bitstring (first 200 bits):", encoded[:200] + ("..." if len(encoded) > 200 else ""))
    print(f"Total bits: {len(encoded)}")
    print("Decoded equals original?", decoded == sample)
