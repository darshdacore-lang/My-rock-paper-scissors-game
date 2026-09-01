def get_target_score():
    """Prompts the player to choose the target winning score."""
    print("\nHow many rounds do you want to win?")
    print("1. Best of 3 (first to 3)")
    print("2. Best of 5 (first to 5)")
    print("3. Best of 10 (first to 10)")
    print("4. Custom")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        return 3
    elif choice == "2":
        return 5
    elif choice == "3":
        return 10
    elif choice == "4":
        while True:
            try:
                custom = int(input("Enter target score: "))
                if custom > 0:
                    return custom
                print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("Invalid choice. Defaulting to 3.")
        return 3