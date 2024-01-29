import re

def word_filter_counter(text, filter_words):
     text_lower = text.lower()
     words = re.findall(r'\b\w+\b', text_lower)
     word_counts = {}

     for word in words:
        if word in filter_words:
            word_counts[word] = word_counts.get(word, 0) + 1

     return word_counts

if __name__ == "__main__":
    text = input (f"Enter text:")
    filter_words = input (f"Enter filter words:")
    result = word_filter_counter(text, filter_words)
    print(result)

# Test cases
print(
    word_filter_counter("Hello world, hello!", ["hello"])
)  # Expected output: {'hello': 2}
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  # Expected output: {'the': 1}
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  # Expected output: {'we': 1, 'the': 1, 'or': 1}
