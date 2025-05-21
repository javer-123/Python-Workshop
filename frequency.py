def find_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

def main():
    user_input = input("Enter a list of elements (space-separated): ")
    try:
        lst = user_input.split()
        frequency = find_frequency(lst)
        print("Frequency of each element:")
        for item, count in frequency.items():
            print(f"{item}: {count}")
    except Exception as e:
        print("An error occurred:", str(e))

if _name_ == "_main_":
    main()
