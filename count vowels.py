def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

def main():
    user_input = input("Enter a string: ")
    vowel_count = count_vowels(user_input)
    print(f"The string contains {vowel_count} vowels.")

if _name_ == "_main_":
    main()
