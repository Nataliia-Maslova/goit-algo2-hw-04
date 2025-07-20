from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise TypeError("Аргумент повинен бути списком рядків")
        
        if not strings:
            return ""

        # Додаємо всі слова у Trie
        for word in strings:
            self.put(word)

        # Проходимо по Trie, поки у кожного вузла лише один нащадок і він не кінцевий
        prefix = ""
        node = self.root

        while True:
            if len(node.children) != 1 or node.value is not None:
                break
            char, next_node = next(iter(node.children.items()))
            prefix += char
            node = next_node

        return prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    print(trie.find_longest_common_word(strings))  # "fl"


    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print(trie.find_longest_common_word(strings))  # "inters"


    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    print(trie.find_longest_common_word(strings))  # ""


    trie = LongestCommonWord()
    strings = []
    print(trie.find_longest_common_word(strings))  # ""
