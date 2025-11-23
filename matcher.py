import difflib
import os

def load_names(file_path='names.txt'):
    """
    Load names from the dataset file.
    Returns a list of lowercase names.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file '{file_path}' not found.")
    
    with open(file_path, 'r') as file:
        names = [line.strip().lower() for line in file if line.strip()]
    
    if len(names) < 30:
        raise ValueError("Dataset must contain at least 30 names.")
    
    return names

def find_matches(input_name, names, threshold=0.6, top_n=5):
    """
    Find similar names using difflib similarity.
    - input_name: The user-input name (str).
    - names: List of dataset names.
    - threshold: Minimum score to consider a match (float).
    - top_n: Number of top matches to return in the ranked list (int).
    
    Returns:
    - best_match: Tuple (name, score) or None if no matches.
    - ranked_matches: List of tuples (name, score) sorted by score descending.
    """
    input_name = input_name.lower()
    similarities = []
    
    for name in names:
        score = difflib.SequenceMatcher(None, input_name, name).ratio()
        if score >= threshold:
            similarities.append((name, score))
    
    # Sort by score descending
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    if not similarities:
        return None, []
    
    # Best match is the first one
    best_match = similarities[0]
    
    # Ranked list excludes the best match if it's exact, but here we include all
    ranked_matches = similarities[1:top_n + 1]  # Top N after best, but adjust if needed
    
    return best_match, ranked_matches