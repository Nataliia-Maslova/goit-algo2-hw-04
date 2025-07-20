from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError("Параметр 'pattern' повинен бути рядком.")
        
        count = 0

        def dfs(node, path):
            nonlocal count
            if node.value is not None:
                if path.endswith(pattern):
                    count += 1
            for char, child in node.children.items():
                dfs(child, path + char)

        dfs(self.root, "")
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("Параметр 'prefix' повинен бути рядком.")
        
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

# Перевірка кількості слів, що закінчуються на заданий суфікс
    print("Suffix 'e':", trie.count_words_with_suffix("e"))         # очікується 1
    print("Suffix 'ion':", trie.count_words_with_suffix("ion"))     # очікується 1
    print("Suffix 'a':", trie.count_words_with_suffix("a"))         # очікується 1
    print("Suffix 'at':", trie.count_words_with_suffix("at"))       # очікується 1

    # Перевірка наявності префікса
    print("Has prefix 'app':", trie.has_prefix("app"))              # очікується True
    print("Has prefix 'bat':", trie.has_prefix("bat"))              # очікується False
    print("Has prefix 'ban':", trie.has_prefix("ban"))              # очікується True
    print("Has prefix 'ca':", trie.has_prefix("ca"))                # очікується True
