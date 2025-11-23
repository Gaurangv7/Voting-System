import sys

class VotingSystem:
    def __init__(self):
        # Dictionary to store candidate names and their vote counts
        self.candidates = {} 
        # List to store IDs of voters who have already voted
        self.voters = []
        # Flag to keep the system running
        self.is_running = True

    def run(self):
        print("---------------------------------------")
        print("   WELCOME TO PYTHON VOTING SYSTEM")
        print("---------------------------------------")
        
        while self.is_running:
            print("\n--- MAIN MENU ---")
            print("1. Admin Login (Set up Election)")
            print("2. Voter Login (Cast Vote)")
            print("3. Show Results")
            print("4. Exit")
            
            try:
                choice = input("Enter option (1-4): ")
                
                if choice == '1':
                    self.admin_panel()
                elif choice == '2':
                    self.voter_panel()
                elif choice == '3':
                    self.show_results()
                elif choice == '4':
                    print("Exiting System... Goodbye!")
                    self.is_running = False
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid Input.")

    def admin_panel(self):
        print("\n--- ADMIN LOGIN ---")
        password = input("Enter Admin Password: ")
        
        # Simple hardcoded password for demonstration
        if password == "admin123":
            while True:
                print("\n[ADMIN DASHBOARD]")
                print("1. Add Candidate")
                print("2. Clear All Votes (Reset)")
                print("3. Back to Main Menu")
                
                choice = input("Select option: ")
                if choice == '1':
                    name = input("Enter Candidate Name: ").strip()
                    if name in self.candidates:
                        print("Candidate already exists!")
                    else:
                        self.candidates[name] = 0
                        print(f"Success: '{name}' added to the ballot.")
                elif choice == '2':
                    confirm = input("Are you sure? (yes/no): ")
                    if confirm.lower() == "yes":
                        self.candidates = {}
                        self.voters = []
                        print("System Reset.")
                elif choice == '3':
                    break
                else:
                    print("Invalid option.")
        else:
            print("Incorrect Password! Access Denied.")

    def voter_panel(self):
        print("\n--- VOTER BOOTH ---")
        
        if not self.candidates:
            print("Error: No candidates found. Please ask Admin to add candidates.")
            return

        # 1. Authenticate Voter
        voter_id = input("Enter your Unique Voter ID (e.g., 101): ").strip()
        
        if voter_id in self.voters:
            print("⚠️  ACCESS DENIED: This ID has already voted.")
            return
        
        # 2. Display Candidates
        print("\nPlease select a candidate:")
        candidate_list = list(self.candidates.keys())
        for i, name in enumerate(candidate_list, 1):
            print(f"{i}. {name}")
            
        # 3. Capture Vote
        try:
            selection = int(input("Enter choice number: "))
            if 1 <= selection <= len(candidate_list):
                selected_candidate = candidate_list[selection - 1]
                
                # Increment vote count
                self.candidates[selected_candidate] += 1
                
                # Mark voter as 'voted'
                self.voters.append(voter_id)
                print(f"✅ Success! Your vote for '{selected_candidate}' has been cast.")
            else:
                print("Invalid number selected.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def show_results(self):
        print("\n--- ELECTION RESULTS ---")
        if not self.candidates:
            print("No votes cast yet.")
            return

        # Sort candidates by votes (High to Low)
        sorted_results = sorted(self.candidates.items(), key=lambda x: x[1], reverse=True)
        
        print(f"{'CANDIDATE':<20} | {'VOTES':<10}")
        print("-" * 30)
        for name, count in sorted_results:
            print(f"{name:<20} | {count:<10}")
        
        # Determine Winner
        winner = sorted_results[0][0]
        max_votes = sorted_results[0][1]
        
        # Check for tie
        if len(sorted_results) > 1 and sorted_results[1][1] == max_votes:
             print(f"\nResult: It is a TIE between top candidates!")
        else:
             print(f"\n🏆 WINNER: {winner} with {max_votes} votes!")

if __name__ == "__main__":
    app = VotingSystem()
    app.run()