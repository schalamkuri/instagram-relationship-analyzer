#!/usr/bin/env python3
"""
Script to compare followers and following lists to find relationships.
"""

import json
import os

def load_usernames_from_json(file_path):
    """
    Load usernames from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing usernames
        
    Returns:
        set: Set of usernames
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            usernames = json.load(file)
            return set(usernames)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return set()
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
        return set()
    except Exception as e:
        print(f"Error loading file '{file_path}': {e}")
        return set()

def load_usernames_from_txt(file_path):
    """
    Load usernames from a text file.
    
    Args:
        file_path (str): Path to the text file containing usernames
        
    Returns:
        set: Set of usernames
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            usernames = set(line.strip() for line in file if line.strip())
            return usernames
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return set()
    except Exception as e:
        print(f"Error loading file '{file_path}': {e}")
        return set()

def analyze_relationships(followers_file, following_file):
    """
    Analyze the relationship between followers and following lists.
    
    Args:
        followers_file (str): Path to followers file
        following_file (str): Path to following file
    """
    print("Loading followers and following lists...")
    
    # Try to load from JSON files first, then fallback to TXT files
    followers = set()
    following = set()
    
    # Load followers
    if os.path.exists(followers_file.replace('.txt', '.json')):
        followers = load_usernames_from_json(followers_file.replace('.txt', '.json'))
        print(f"Loaded {len(followers)} followers from JSON file")
    elif os.path.exists(followers_file):
        followers = load_usernames_from_txt(followers_file)
        print(f"Loaded {len(followers)} followers from TXT file")
    else:
        print(f"Error: Could not find followers file")
        return
    
    # Load following
    if os.path.exists(following_file.replace('.txt', '.json')):
        following = load_usernames_from_json(following_file.replace('.txt', '.json'))
        print(f"Loaded {len(following)} following from JSON file")
    elif os.path.exists(following_file):
        following = load_usernames_from_txt(following_file)
        print(f"Loaded {len(following)} following from TXT file")
    else:
        print(f"Error: Could not find following file")
        return
    
    if not followers or not following:
        print("Error: Could not load data from files")
        return
    
    print("\n" + "="*60)
    print("RELATIONSHIP ANALYSIS")
    print("="*60)
    
    # Find mutual followers (people who follow you AND you follow them)
    mutual_followers = followers.intersection(following)
    print(f"\n✅ MUTUAL FOLLOWERS: {len(mutual_followers)}")
    print("   (People who follow you AND you follow them)")
    
    # Find people you follow who don't follow you back
    not_following_back = following.difference(followers)
    print(f"\n❌ NOT FOLLOWING YOU BACK: {len(not_following_back)}")
    print("   (People you follow but they don't follow you)")
    
    # Find people who follow you but you don't follow back
    you_dont_follow_back = followers.difference(following)
    print(f"\n👥 YOU DON'T FOLLOW BACK: {len(you_dont_follow_back)}")
    print("   (People who follow you but you don't follow them)")
    
    # Show some examples
    print("\n" + "-"*40)
    print("EXAMPLES:")
    
    if mutual_followers:
        print(f"\nMutual followers (first 5): {list(sorted(mutual_followers))[:5]}")
    
    if not_following_back:
        print(f"\nNot following you back (first 5): {list(sorted(not_following_back))[:5]}")
    
    if you_dont_follow_back:
        print(f"\nYou don't follow back (first 5): {list(sorted(you_dont_follow_back))[:5]}")
    
    # Save consolidated results to a single file
    print("\n" + "-"*40)
    print("SAVING CONSOLIDATED ANALYSIS:")
    
    try:
        with open("relationship_analysis.txt", 'w', encoding='utf-8') as file:
            # Write header
            file.write("="*80 + "\n")
            file.write("INSTAGRAM RELATIONSHIP ANALYSIS\n")
            file.write("="*80 + "\n\n")
            
            # Write summary
            file.write("SUMMARY:\n")
            file.write("-"*40 + "\n")
            file.write(f"Total Followers: {len(followers)}\n")
            file.write(f"Total Following: {len(following)}\n")
            file.write(f"Mutual Followers: {len(mutual_followers)}\n")
            file.write(f"Not Following You Back: {len(not_following_back)}\n")
            file.write(f"You Don't Follow Back: {len(you_dont_follow_back)}\n\n")
            
            # Write mutual followers section
            file.write("="*80 + "\n")
            file.write(f"✅ MUTUAL FOLLOWERS ({len(mutual_followers)})\n")
            file.write("People who follow you AND you follow them\n")
            file.write("="*80 + "\n")
            if mutual_followers:
                for username in sorted(mutual_followers):
                    file.write(f"{username}\n")
            else:
                file.write("None\n")
            file.write("\n")
            
            # Write not following back section
            file.write("="*80 + "\n")
            file.write(f"❌ NOT FOLLOWING YOU BACK ({len(not_following_back)})\n")
            file.write("People you follow but they don't follow you\n")
            file.write("="*80 + "\n")
            if not_following_back:
                for username in sorted(not_following_back):
                    file.write(f"{username}\n")
            else:
                file.write("None\n")
            file.write("\n")
            
            # Write you don't follow back section
            file.write("="*80 + "\n")
            file.write(f"👥 YOU DON'T FOLLOW BACK ({len(you_dont_follow_back)})\n")
            file.write("People who follow you but you don't follow them\n")
            file.write("="*80 + "\n")
            if you_dont_follow_back:
                for username in sorted(you_dont_follow_back):
                    file.write(f"{username}\n")
            else:
                file.write("None\n")
            file.write("\n")
            
            # Write footer
            file.write("="*80 + "\n")
            file.write("END OF ANALYSIS\n")
            file.write("="*80 + "\n")
        
        print(f"✅ Saved complete analysis to 'relationship_analysis.txt'")
        
    except Exception as e:
        print(f"Error saving consolidated analysis: {e}")
    
    # Also save as JSON for programmatic access
    try:
        with open("relationship_analysis.json", 'w', encoding='utf-8') as file:
            analysis_data = {
                "summary": {
                    "total_followers": len(followers),
                    "total_following": len(following),
                    "mutual_followers": len(mutual_followers),
                    "not_following_back": len(not_following_back),
                    "you_dont_follow_back": len(you_dont_follow_back)
                },
                "mutual_followers": sorted(list(mutual_followers)),
                "not_following_back": sorted(list(not_following_back)),
                "you_dont_follow_back": sorted(list(you_dont_follow_back))
            }
            json.dump(analysis_data, file, indent=2, ensure_ascii=False)
        print("✅ Also saved JSON version to 'relationship_analysis.json'")
    except Exception as e:
        print(f"Error saving JSON analysis: {e}")
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)

def main():
    """Main function to run the relationship analysis."""
    followers_file = "followers_usernames.txt"
    following_file = "following_usernames.txt"
    
    print("Instagram Relationship Analyzer")
    print("="*60)
    
    analyze_relationships(followers_file, following_file)

if __name__ == "__main__":
    main()
