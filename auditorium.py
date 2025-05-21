num_rows = int(input("Enter number of rows: "))
s1, s2, s3 = 6, 10, 6
total_seats = s1 + s2 + s3
auditorium = [["-" for _ in range(total_seats)] for _ in range(num_rows)]
def seat_index(section, seat):
    if section == 1 and 1 <= seat <= s1: return seat - 1
    if section == 2 and 1 <= seat <= s2: return s1 + seat - 1
    if section == 3 and 1 <= seat <= s3: return s1 + s2 + seat - 1
    return -1
def modify_seat(row, index, action):
    if 0 <= row < num_rows and 0 <= index < total_seats:
        if action == "book" and auditorium[row][index] == "-":
            auditorium[row][index] = "*"; print("Seat booked.")
        elif action == "cancel" and auditorium[row][index] == "*":
            auditorium[row][index] = "-"; print("Seat cancelled.")
        else: print("Action not possible.")
    else: print("Invalid seat.")
def display():
    print("\nSeating Arrangement:")
    for row in auditorium:
        print("".join(f" {s}" + ("  " if i in [s1-1, s1+s2-1] else "") for i, s in enumerate(row)))
while True:
    display()
    choice = input("\nBook or Cancel a seat? (book/cancel/exit): ").lower()
    if choice == "exit": break
    row = int(input(f"Enter row (1-{num_rows}): ")) - 1
    section = int(input("Enter section (1-3): "))
    seat = int(input("Enter seat number in section: "))
    index = seat_index(section, seat)
    if index == -1: print("Invalid seat."); continue
    modify_seat(row, index, choice)
print("\nFinal Seating Arrangement:")
display()
