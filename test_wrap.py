# TEST to see which line limit looks best

from progressive_bible_verses import wrap_text

test_verse = "There is neither Jew nor Greek, there is neither slave nor free man, there is neither male nor female; for you are all one in Christ Jesus."

print("\n--- Testing width=60 ---")
for line in wrap_text(f'"{test_verse}..."', width=60):
    print(line)

print("\n--- Testing width=50 ---")
for line in wrap_text(f'"{test_verse}..."', width=50):
    print(line)