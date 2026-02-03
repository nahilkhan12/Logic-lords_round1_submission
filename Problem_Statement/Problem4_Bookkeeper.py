def verify_bookkeeper_math():
    word = "Bookkeeper"
    
    # 1. Find pairs of identical consecutive characters
    pairs_count = 0
    pairs = []
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            pairs_count += 1
            pairs.append(word[i] + word[i+1])
            
    # 2. Count total occurrences of 'e'
    e_count = word.count('e')
    
    # 3. Multiply the counts
    result = pairs_count * e_count
    
    print(f"Word: {word}")
    print(f"Consecutive identical pairs found: {pairs} (Count: {pairs_count})")
    print(f"Total occurrences of 'e': {e_count}")
    print(f"Final calculation ({pairs_count} * {e_count}): {result}")

if __name__ == "__main__":
    verify_bookkeeper_math()