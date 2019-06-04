import os
import re

# To make a node
class TrieNode(object):
    # default constructor
    def __init__(self, char):
        self.char = char
        self.children = []
        self.is_end_of_word = False  # Is it the last character of the word.
        self.counter = 1  # How many times this character appeared in the addition process
        self.file_name = []
        self.index = []


# Reading, cleaning and taking words from files
def read_files(root):
    for file_name in os.listdir(os.getcwd() + "/sampleTextFiles"):
        input_data = open(os.getcwd() + "/sampleTextFiles/" + file_name, 'r').read()
        words = input_data.split()
        index = 1
        for word in words:
            length = len(word)
            word = re.sub(r'[^\w\s]', '', word) # Clean words from punc.
            add(root, word, file_name, index)
            index += length + 1


# To add word to the trie
def add(root, word, file_name, index):
    node = root
    for char in word:
        found_in_child = False

        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break

        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node

    node.is_end_of_word = True
    node.file_name.append(file_name)
    node.index.append(index)


# To check whether a word is in trie
def find(root, prefix):
    case1 = prefix.capitalize()  # Capital prefix
    case2 = prefix.lower()  # Lower case prefix
    case3 = prefix.upper()  # Upper case prefix
    find_prefix(root, case1)
    find_prefix(root, case2)
    find_prefix(root, case3)


# It goes all path with prefix characters
def find_prefix(root, prefix):
    node = root
    if not root.children:
        return
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return

    print_words(node, prefix)


# It takes the node which is reached with obtained prefix
# Then tries to look at all children and prints they
def print_words(root, prefix):
    node = root
    if not node.children:
        print "\n" + prefix + ":"
        for i in range(len(node.file_name)):
            print node.file_name[i], node.index[i]
        return
    if node.is_end_of_word:
        print "\n" + prefix + ":"
        for i in range(len(node.file_name)):
            print node.file_name[i], node.index[i]
    for child in node.children:
        if child.is_end_of_word:
            print_words(child, (prefix + child.char))
        else:
            print_words(child, (prefix + child.char))


# To search common words in obtained files
def common_words(root, file_names, word):
    node = root
    if not node.children:
        return
    for child in node.children:
        if child.is_end_of_word and all(elem in child.file_name for elem in file_names):
            print word + child.char
            common_words(child, file_names, word + child.char)
        else:
            common_words(child, file_names, word + child.char)

# Takes desired option of the program and runs it
def main():
    root = TrieNode('*')
    read_files(root)

    query_type = raw_input('Enter 1 to search words with entering a prefix\n' +
                           'Enter 2 to search common words of desired files\n' +
                           'What do you want to do? ')

    if query_type == "1":
        prefix = raw_input("Enter a prefix: ")
        find(root, prefix)
    else:
        file_names = raw_input("Enter file names to search common words: ")
        common_words(root, file_names.split(), "")


# To run main function
if __name__ == '__main__':
    main()
