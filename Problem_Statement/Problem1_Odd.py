def number_to_words(n):
    """
    Converts a number (up to 10,000) into its English word representation.
    """
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 0:
        return "zero"
    
    parts = []
    
    # Handle Thousands
    if n >= 1000:
        parts.append(ones[n // 1000] + " thousand")
        n %= 1000
    
    # Handle Hundreds
    if n >= 100:
        parts.append(ones[n // 100] + " hundred")
        n %= 100
    
    # Handle Tens and Ones
    if n >= 20:
        parts.append(tens[n // 10])
        n %= 10
    elif n >= 10:
        parts.append(teens[n - 10])
        n = 0
        
    if n > 0:
        parts.append(ones[n])
        
    return " ".join(parts)

def find_odd_numbers_without_e(limit):
    found_any = False
    
    print(f"Checking the first {limit:,} integers...")
    
    for i in range(1, limit + 1):
        # 1. Check if it is Odd
        if i % 2 != 0:
            # 2. Convert to English word
            word = number_to_words(i)
            
            # 3. Check if 'e' is absent
            if 'e' not in word and 'E' not in word:
                print(f"Match found: {i} ({word})")
                found_any = True
                
    # 4. Final output if list is empty
    if not found_any:
        print("No odd numbers found without letter e")

if __name__ == "__main__":
    find_odd_numbers_without_e(10000)