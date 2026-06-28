#!/usr/bin/env python3
"""
Instagram Relationship Analyzer - Complete Solution
This script extracts followers and following data from Instagram JSON exports
and performs a comprehensive relationship analysis.
"""

import json
import os
from datetime import datetime

def extract_followers_from_json(json_file_path):
    """
    Extract all usernames from the followers JSON file.
    
    Args:
        json_file_path (str): Path to the followers JSON file
        
    Returns:
        set: Set of follower usernames
    """
    usernames = set()
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        # Iterate through each entry in the JSON array
        for entry in data:
            # Check if string_list_data exists and is not empty
            if 'string_list_data' in entry and entry['string_list_data']:
                # Extract the value (username) from each item in string_list_data
                for string_data in entry['string_list_data']:
                    if 'value' in string_data:
                        usernames.add(string_data['value'])
                        
    except FileNotFoundError:
        print(f"❌ Error: File '{json_file_path}' not found.")
        return set()
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON format in '{json_file_path}'.")
        return set()
    except Exception as e:
        print(f"❌ Error processing followers file: {e}")
        return set()
    
    return usernames

def extract_following_from_json(json_file_path):
    """
    Extract all usernames from the following JSON file.
    
    Args:
        json_file_path (str): Path to the following JSON file
        
    Returns:
        set: Set of following usernames
    """
    usernames = set()
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        # Check if relationships_following exists in the data
        if 'relationships_following' in data:
            # Iterate through each entry in the relationships_following array
            for entry in data['relationships_following']:
                # Skip empty objects or entries without required fields
                if not entry or not isinstance(entry, dict):
                    continue
                
                # The username is in the 'title' field
                if 'title' in entry:
                    username = entry['title']
                    # Only add non-empty usernames
                    if username and isinstance(username, str):
                        usernames.add(username.strip())
                # Fallback: check string_list_data for 'value' field (older format)
                elif 'string_list_data' in entry and entry['string_list_data']:
                    for string_data in entry['string_list_data']:
                        if isinstance(string_data, dict) and 'value' in string_data:
                            username = string_data['value']
                            if username and isinstance(username, str):
                                usernames.add(username.strip())
        else:
            print("❌ Error: 'relationships_following' key not found in the following JSON file.")
            return set()
                        
    except FileNotFoundError:
        print(f"❌ Error: File '{json_file_path}' not found.")
        return set()
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON format in '{json_file_path}'.")
        return set()
    except Exception as e:
        print(f"❌ Error processing following file: {e}")
        return set()
    
    return usernames

def save_usernames_to_files(usernames, prefix):
    """
    Save usernames to both TXT and JSON files.
    
    Args:
        usernames (set): Set of usernames
        prefix (str): File prefix (e.g., 'followers', 'following')
    """
    try:
        # Save as text file
        txt_file = f"{prefix}_usernames.txt"
        with open(txt_file, 'w', encoding='utf-8') as file:
            for username in sorted(usernames):
                file.write(f"{username}\n")
        print(f"✅ Saved {len(usernames)} usernames to '{txt_file}'")
        
        # Save as JSON file
        json_file = f"{prefix}_usernames.json"
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(sorted(list(usernames)), file, indent=2, ensure_ascii=False)
        print(f"✅ Saved {len(usernames)} usernames to '{json_file}'")
        
    except Exception as e:
        print(f"❌ Error saving {prefix} files: {e}")

def create_relationship_analysis(followers, following):
    """
    Create comprehensive relationship analysis and save to files.
    
    Args:
        followers (set): Set of follower usernames
        following (set): Set of following usernames
    """
    # Calculate relationships
    mutual_followers = followers.intersection(following)
    not_following_back = following.difference(followers)
    you_dont_follow_back = followers.difference(following)
    
    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save consolidated text analysis
    try:
        with open("relationship_analysis.txt", 'w', encoding='utf-8') as file:
            # Write header
            file.write("="*80 + "\n")
            file.write("INSTAGRAM RELATIONSHIP ANALYSIS\n")
            file.write("="*80 + "\n")
            file.write(f"Generated on: {timestamp}\n\n")
            
            # Write summary
            file.write("SUMMARY:\n")
            file.write("-"*40 + "\n")
            file.write(f"Total Followers: {len(followers):,}\n")
            file.write(f"Total Following: {len(following):,}\n")
            file.write(f"Mutual Followers: {len(mutual_followers):,}\n")
            file.write(f"Not Following You Back: {len(not_following_back):,}\n")
            file.write(f"You Don't Follow Back: {len(you_dont_follow_back):,}\n\n")
            
            # Calculate percentages
            if len(following) > 0:
                mutual_percentage = (len(mutual_followers) / len(following)) * 100
                not_following_back_percentage = (len(not_following_back) / len(following)) * 100
            else:
                mutual_percentage = 0
                not_following_back_percentage = 0
                
            if len(followers) > 0:
                you_dont_follow_back_percentage = (len(you_dont_follow_back) / len(followers)) * 100
            else:
                you_dont_follow_back_percentage = 0
            
            file.write("PERCENTAGES:\n")
            file.write("-"*40 + "\n")
            file.write(f"Mutual Follow Rate: {mutual_percentage:.1f}%\n")
            file.write(f"Not Following Back Rate: {not_following_back_percentage:.1f}%\n")
            file.write(f"You Don't Follow Back Rate: {you_dont_follow_back_percentage:.1f}%\n\n")
            
            # Write mutual followers section
            file.write("="*80 + "\n")
            file.write(f"✅ MUTUAL FOLLOWERS ({len(mutual_followers):,})\n")
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
            file.write(f"❌ NOT FOLLOWING YOU BACK ({len(not_following_back):,})\n")
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
            file.write(f"👥 YOU DON'T FOLLOW BACK ({len(you_dont_follow_back):,})\n")
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
        print(f"❌ Error saving text analysis: {e}")
    
    # Save JSON analysis
    try:
        with open("relationship_analysis.json", 'w', encoding='utf-8') as file:
            analysis_data = {
                "generated_on": timestamp,
                "summary": {
                    "total_followers": len(followers),
                    "total_following": len(following),
                    "mutual_followers": len(mutual_followers),
                    "not_following_back": len(not_following_back),
                    "you_dont_follow_back": len(you_dont_follow_back),
                    "mutual_follow_rate": round(mutual_percentage, 1),
                    "not_following_back_rate": round(not_following_back_percentage, 1),
                    "you_dont_follow_back_rate": round(you_dont_follow_back_percentage, 1)
                },
                "mutual_followers": sorted(list(mutual_followers)),
                "not_following_back": sorted(list(not_following_back)),
                "you_dont_follow_back": sorted(list(you_dont_follow_back))
            }
            json.dump(analysis_data, file, indent=2, ensure_ascii=False)
        print("✅ Saved JSON analysis to 'relationship_analysis.json'")
    except Exception as e:
        print(f"❌ Error saving JSON analysis: {e}")
    
    return mutual_followers, not_following_back, you_dont_follow_back

def main():
    """Main function to run the complete Instagram relationship analysis."""
    print("="*80)
    print("INSTAGRAM RELATIONSHIP ANALYZER - COMPLETE SOLUTION")
    print("="*80)
    print()
    
    # File paths for Instagram JSON exports
    followers_file = "followers_1.json"
    following_file = "following.json"
    
    # Step 1: Extract followers
    print("📥 STEP 1: Extracting followers...")
    print("-" * 40)
    followers = extract_followers_from_json(followers_file)
    
    if followers:
        print(f"✅ Found {len(followers):,} followers!")
        save_usernames_to_files(followers, "followers")
    else:
        print("❌ Failed to extract followers. Exiting...")
        return
    
    print()
    
    # Step 2: Extract following
    print("📥 STEP 2: Extracting following...")
    print("-" * 40)
    following = extract_following_from_json(following_file)
    
    if following:
        print(f"✅ Found {len(following):,} accounts you're following!")
        save_usernames_to_files(following, "following")
    else:
        print("❌ Failed to extract following. Exiting...")
        return
    
    print()
    
    # Step 3: Relationship Analysis
    print("🔍 STEP 3: Analyzing relationships...")
    print("-" * 40)
    
    mutual_followers, not_following_back, you_dont_follow_back = create_relationship_analysis(followers, following)
    
    # Display summary
    print(f"✅ Analysis complete!")
    print()
    print("📊 SUMMARY:")
    print(f"   Followers: {len(followers):,}")
    print(f"   Following: {len(following):,}")
    print(f"   Mutual: {len(mutual_followers):,}")
    print(f"   Not Following Back: {len(not_following_back):,}")
    print(f"   You Don't Follow Back: {len(you_dont_follow_back):,}")
    
    # Show examples if there are non-mutual relationships
    if not_following_back:
        print(f"\n❌ Examples of accounts not following you back:")
        for username in sorted(list(not_following_back))[:5]:
            print(f"   • {username}")
        if len(not_following_back) > 5:
            print(f"   ... and {len(not_following_back) - 5} more")
    
    if you_dont_follow_back:
        print(f"\n👥 Examples of accounts you don't follow back:")
        for username in sorted(list(you_dont_follow_back))[:5]:
            print(f"   • {username}")
        if len(you_dont_follow_back) > 5:
            print(f"   ... and {len(you_dont_follow_back) - 5} more")
    
    print()
    print("="*80)
    print("📁 FILES CREATED:")
    print("-" * 40)
    print("• followers_usernames.txt & .json")
    print("• following_usernames.txt & .json") 
    print("• relationship_analysis.txt")
    print("• relationship_analysis.json")
    print("="*80)
    print("✅ ANALYSIS COMPLETE! Check the files above for detailed results.")
    print("="*80)

if __name__ == "__main__":
    main()
