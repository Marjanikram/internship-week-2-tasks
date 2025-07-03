print("Enter marks out of 100 for 5 subjects:")
try:
    m1 = int(input("Subject 1: "))
    m2 = int(input("Subject 2: "))
    m3 = int(input("Subject 3: "))
    m4 = int(input("Subject 4: "))
    m5 = int(input("Subject 5: "))
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5
    print(f"\nTotal Marks: {total}/500")
    print(f"Percentage: {percentage}%")
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    else:
        grade = "Fail"
    print(f"Grade: {grade}")
except ValueError:
    print("Please enter only numeric values for marks.")