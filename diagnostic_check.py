#!/usr/bin/env python3
"""
Diagnostic script to check the JSON file formats and parsing
"""

import json

def diagnose_followers():
    print("="*60)
    print("DIAGNOSING FOLLOWERS_1.JSON")
    print("="*60)
    
    with open('followers_1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Type of data: {type(data)}")
    print(f"Number of entries: {len(data)}")
    print(f"\nFirst entry structure:")
    print(json.dumps(data[0], indent=2))
    
    # Count valid usernames
    valid_count = 0
    sample_usernames = []
    for entry in data:
        if 'string_list_data' in entry and entry['string_list_data']:
            for string_data in entry['string_list_data']:
                if 'value' in string_data:
                    valid_count += 1
                    if len(sample_usernames) < 10:
                        sample_usernames.append(string_data['value'])
    
    print(f"\nValid usernames found: {valid_count}")
    print(f"Sample usernames (first 10):")
    for username in sample_usernames:
        print(f"  • {username}")
    print()

def diagnose_following():
    print("="*60)
    print("DIAGNOSING FOLLOWING.JSON")
    print("="*60)
    
    with open('following.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Type of data: {type(data)}")
    print(f"Has 'relationships_following': {'relationships_following' in data}")
    
    if 'relationships_following' in data:
        following_list = data['relationships_following']
        print(f"Number of entries in relationships_following: {len(following_list)}")
        print(f"\nFirst entry structure:")
        if following_list:
            print(json.dumps(following_list[0], indent=2))
        
        # Count valid usernames
        valid_count = 0
        empty_count = 0
        sample_usernames = []
        
        for entry in following_list:
            if entry and isinstance(entry, dict) and 'title' in entry:
                username = entry['title']
                if username and isinstance(username, str) and username.strip():
                    valid_count += 1
                    if len(sample_usernames) < 10:
                        sample_usernames.append(username)
                else:
                    empty_count += 1
            else:
                empty_count += 1
        
        print(f"\nValid usernames found: {valid_count}")
        print(f"Empty/invalid entries: {empty_count}")
        print(f"Sample usernames (first 10):")
        for username in sample_usernames:
            print(f"  • {username}")
    print()

def compare_datasets():
    print("="*60)
    print("COMPARING DATASETS")
    print("="*60)
    
    # Load followers
    with open('followers_1.json', 'r', encoding='utf-8') as f:
        followers_data = json.load(f)
    
    followers = set()
    for entry in followers_data:
        if 'string_list_data' in entry and entry['string_list_data']:
            for string_data in entry['string_list_data']:
                if 'value' in string_data:
                    followers.add(string_data['value'])
    
    # Load following
    with open('following.json', 'r', encoding='utf-8') as f:
        following_data = json.load(f)
    
    following = set()
    if 'relationships_following' in following_data:
        for entry in following_data['relationships_following']:
            if entry and isinstance(entry, dict) and 'title' in entry:
                username = entry['title']
                if username and isinstance(username, str):
                    following.add(username.strip())
    
    print(f"Total followers extracted: {len(followers)}")
    print(f"Total following extracted: {len(following)}")
    
    # Check for common usernames
    common = followers.intersection(following)
    only_followers = followers - following
    only_following = following - followers
    
    print(f"\nCommon accounts (mutual): {len(common)}")
    print(f"Only in followers: {len(only_followers)}")
    print(f"Only in following: {len(only_following)}")
    
    print(f"\nSample mutual followers:")
    for username in sorted(list(common))[:10]:
        print(f"  • {username}")
    
    print(f"\nSample accounts not following back:")
    for username in sorted(list(only_following))[:10]:
        print(f"  • {username}")
    
    print(f"\nSample accounts you don't follow back:")
    for username in sorted(list(only_followers))[:10]:
        print(f"  • {username}")

if __name__ == "__main__":
    diagnose_followers()
    diagnose_following()
    compare_datasets()
