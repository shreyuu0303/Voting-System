
candidates = ["Shreyas","Tejas","Ram","Raaj","Krushna","Bajirao","Vitthalrao","Rajan","Sahil1"]
votes = {candidate: 0 for candidate in candidates}

def cast_vote():
    print("\nVote for a candidate:")
    for i, name in enumerate(candidates, 1):
        print(f"{i}. {name}")

    choice = int(input("Enter your choice (1–{}): ".format(len(candidates))))
    if 1 <= choice <= len(candidates):
        selected = candidates[choice - 1]
        votes[selected] += 1
        print(f"✅ Vote cast for {selected}!")
    else:
        print("❌ Invalid choice. Try again.")


def show_results():
    print("\n📊 Vote Count:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")



def show_winner():
    max_votes = max(votes.values())
    winners = [name for name, count in votes.items() if count == max_votes]

    print("\n🏆 Winner(s):")
    for winner in winners:
        print(f"{winner} with {max_votes} votes")



while True:
    print("\n🔘 Menu:\n1. Cast Vote\n2. Show Results\n3. Show Winner\n4. Exit")
    option = input("Enter your option: ")

    if option == '1':
        cast_vote()
    elif option == '2':
        show_results()
    elif option == '3':
        show_winner()
    elif option == '4':
        print("🚪 Exiting Voting System. Thank you!")
        break
    else:
        print("❌ Invalid input. Try again.")
