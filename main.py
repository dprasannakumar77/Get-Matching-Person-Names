from matcher import load_names, find_matches

def main():
    # Load the dataset
    try:
        names = load_names()
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return
    
    # Get user input
    input_name = input("Enter a name to match: ").strip()
    if not input_name:
        print("Error: Please enter a valid name.")
        return
    
    # Find matches
    best_match, ranked_matches = find_matches(input_name, names)
    
    # Display output
    print("\nExpected Output:")
    if best_match:
        print(f"• Best Match: {best_match[0].capitalize()} with similarity score {best_match[1]:.2f}")
    else:
        print("• Best Match: No close matches found.")
    
    print("• List of Matches:")
    if ranked_matches:
        for i, (name, score) in enumerate(ranked_matches, 1):
            print(f"  {i}. {name.capitalize()} (score: {score:.2f})")
    else:
        print("  No other similar matches found.")

if __name__ == "__main__":
    main()