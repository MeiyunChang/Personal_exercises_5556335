def speeding_ticket(speed, is_birthday):
    if is_birthday:
        no_ticket = 65
        small_ticket = 85
    else:
        no_ticket = 60
        small_ticket = 80
    
    if speed <= no_ticket:
        return "No Ticket"
    elif speed <= small_ticket:
        return "Small Ticket"
    else:
        return "Big Ticket"

if __name__ == "__main__":
    speed = int (input ("The speed is:"))
    is_birthday = input (f"True/False:")
    result = speeding_ticket(speed, is_birthday)
    print(result)


# Test cases
speeding_ticket(60, False)  # Expected output: "No Ticket"
speeding_ticket(75, False)  # Expected output: "Small Ticket"
speeding_ticket(85, False)  # Expected output: "Big Ticket"
speeding_ticket(65, True)  # Expected output: "No Ticket"
speeding_ticket(85, True)  # Expected output: "Small Ticket"
