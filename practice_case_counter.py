def case_counter(text):
    uppercase_count = 0
    lowercase_count = 0
     
    for char in text:
        if char.isalpha():
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
    
    print(f"Uppercase letters count:", {uppercase_count})
    print(f"Lowercase letters count:", {lowercase_count})

def Counter():
    while True:
        print("Case Counter")
        print ("1. Counter")
        print("2. Exit")
        choice = input("Enter choice (1/2): ")
        
        if choice == "1":
            input_content = input ("Enter content:")
            output_content = case_counter(input_content)
            print(f"{input_content} : {output_content}")

        elif choice == "2":
            print ("Exit from the system")
            break

        else:
            print ("Invaild input, please try again.")

if __name__ == "__main__":
    Counter()

# Test cases
case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON")  # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python")  # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")  # Expected: Uppercase letters: 0, Lowercase letters: 0
