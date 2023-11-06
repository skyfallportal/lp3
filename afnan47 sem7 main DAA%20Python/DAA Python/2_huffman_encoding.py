import heapq

# Creating Huffman tree node
class node:
    def __init__(self,freq,symbol,left=None,right=None):
        self.freq=freq # frequency of symbol
        self.symbol=symbol # symbol name (character)
        self.left=left # node left of current node
        self.right=right # node right of current node
        self.huff= '' # # tree direction (0/1)

    def __lt__(self,nxt): # Check if curr frequency less than next nodes freq
        return self.freq<nxt.freq

def printnodes(node,val=''):
    newval=val+str(node.huff)
    # if node is not an edge node then traverse inside it
    if node.left: 
        printnodes(node.left,newval)
    if node.right: 
        printnodes(node.right,newval)

    # if node is edge node then display its huffman code
    if not node.left and not node.right:
        print("{} -> {}".format(node.symbol,newval))

if __name__=="__main__":
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [ 5, 9, 12, 13, 16, 45]
    nodes=[]    

    for i in range(len(chars)): # converting characters and frequencies into huffman tree nodes
        heapq.heappush(nodes, node(freq[i],chars[i]))

    while len(nodes)>1:
        left=heapq.heappop(nodes)
        right=heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1
        # Combining the 2 smallest nodes to create new node as their parent
        newnode = node(left.freq + right.freq , left.symbol + right.symbol , left , right)
        # node(freq,symbol,left,right)
        heapq.heappush(nodes, newnode)

    printnodes(nodes[0]) # Passing root of Huffman Tree

    
    '''
    This code implements the Huffman coding algorithm, a lossless data compression algorithm, to construct a variable-length prefix coding tree (Huffman tree) for a set of characters based on their frequencies. The Huffman tree is used to generate optimal binary codes for each character such that characters with higher frequencies are assigned shorter codes, reducing the overall storage or transmission size.

Here's the code with comments explaining it line by line:


Explanation of the concept used in this code:

- The code constructs a Huffman tree by iteratively combining the two smallest nodes (symbols with the lowest frequencies) into a new parent node with the sum of their frequencies. The binary representation (0 or 1) is assigned to the left and right child nodes, and this process continues until there is only one node left, which becomes the root of the Huffman tree.

- The `printnodes` function recursively traverses the Huffman tree to generate and print the Huffman codes for each character. A Huffman code is a binary representation where the path from the root to each leaf node corresponds to a unique code for a character, with left branches represented as '0' and right branches as '1'.

- The code uses a min-heap (a priority queue) to efficiently select the two smallest nodes for merging, ensuring that the nodes with the lowest frequencies are always processed first.

- The Huffman coding algorithm is used in data compression, file formats, and various other applications to achieve efficient and lossless data encoding.
    '''



'''
A Huffman tree, also known as a Huffman coding tree, is a binary tree used in data compression algorithms, specifically in Huffman coding. Huffman coding is a lossless data compression technique that assigns variable-length binary codes to characters in a way that minimizes the total number of bits required to represent a sequence of characters. It is commonly used in file compression formats like ZIP and in other applications where data compression is necessary.

Here's how a Huffman tree and Huffman coding work:

1. **Frequency Analysis:** In the first step, the frequencies of characters (or symbols) in the input data are analyzed. This means counting how often each character appears in the data.

2. **Building the Huffman Tree:** The Huffman tree is constructed based on the character frequencies. The tree is built in a way that characters with higher frequencies are closer to the root of the tree, while characters with lower frequencies are deeper in the tree.

    - Start with a forest of single-node trees, where each tree represents a character and its frequency.
    - Repeatedly merge the two trees with the lowest frequencies into a new tree with a frequency equal to the sum of the merged trees.
    - Assign '0' to the left branch and '1' to the right branch of the merged tree.
    - Continue merging until there is only one tree left, which becomes the Huffman tree.

3. **Huffman Coding:** Once the Huffman tree is constructed, each character is represented by a unique path from the root of the tree to the leaf node that corresponds to that character. This path is called the Huffman code for that character.

    - Characters closer to the root have shorter codes, and characters farther from the root have longer codes.
    - The Huffman code for each character is generated by recording the '0' and '1' values encountered while traversing the tree from the root to the character's leaf node.

4. **Data Compression:** To compress data, replace the original characters with their corresponding Huffman codes. The result is a compressed version of the data, where characters with higher frequencies are represented by shorter codes, resulting in overall data compression.

5. **Decompression:** To decompress the data, use the Huffman tree to reverse the process. Start from the root and follow the path defined by the received binary codes to reconstruct the original characters.

Huffman coding is known for its efficiency in representing frequently occurring characters with shorter codes, reducing the size of compressed data. Huffman trees are used to decode and encode data efficiently, making them a fundamental concept in data compression and encoding algorithms.
'''