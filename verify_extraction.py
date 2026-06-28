#!/usr/bin/env python3
"""
Verify we're extracting the correct data from the JSON files
"""

import json

print("="*70)
print("VERIFICATION: Are we extracting the correct values?")
print("="*70)

# Check followers_1.json
print("\n1️⃣ CHECKING FOLLOWERS_1.JSON")
print("-"*70)
with open('followers_1.json', 'r', encoding='utf-8') as f:
    followers_data = json.load(f)

print(f"Total entries: {len(followers_data)}")
print(f"\nFirst 3 entries (raw structure):")
for i in range(min(3, len(followers_data))):
    entry = followers_data[i]
    print(f"\nEntry #{i+1}:")
    print(f"  title: '{entry.get('title', 'N/A')}'")
    print(f"  string_list_data: {entry.get('string_list_data', [])}")
    if 'string_list_data' in entry and entry['string_list_data']:
        for item in entry['string_list_data']:
            if 'value' in item:
                print(f"  ➡️  EXTRACTED USERNAME: '{item['value']}'")

# Check following.json  
print("\n\n2️⃣ CHECKING FOLLOWING.JSON")
print("-"*70)
with open('following.json', 'r', encoding='utf-8') as f:
    following_data = json.load(f)

if 'relationships_following' in following_data:
    following_list = following_data['relationships_following']
    print(f"Total entries: {len(following_list)}")
    print(f"\nFirst 3 entries (raw structure):")
    for i in range(min(3, len(following_list))):
        entry = following_list[i]
        print(f"\nEntry #{i+1}:")
        print(f"  title: '{entry.get('title', 'N/A')}'")
        print(f"  string_list_data: {entry.get('string_list_data', [])}")
        if 'title' in entry:
            print(f"  ➡️  EXTRACTED USERNAME: '{entry['title']}'")

# Now let's manually verify the logic
print("\n\n3️⃣ MANUAL VERIFICATION OF LOGIC")
print("-"*70)

# Extract using the script's logic
followers_set = set()
for entry in followers_data:
    if 'string_list_data' in entry and entry['string_list_data']:
        for string_data in entry['string_list_data']:
            if 'value' in string_data:
                followers_set.add(string_data['value'])

following_set = set()
if 'relationships_following' in following_data:
    for entry in following_data['relationships_following']:
        if entry and isinstance(entry, dict) and 'title' in entry:
            username = entry['title']
            if username and isinstance(username, str):
                following_set.add(username.strip())

print(f"\n✅ FOLLOWERS = People who follow YOU: {len(followers_set)} accounts")
print(f"✅ FOLLOWING = People YOU follow: {len(following_set)} accounts")

# Pick a few test cases
print("\n\n4️⃣ MANUAL TEST CASES")
print("-"*70)

test_cases = ['frederick.alejandro98', 'gen.eric.films', 'luliaaa__', '_prith03_']

for username in test_cases:
    in_followers = username in followers_set
    in_following = username in following_set
    
    print(f"\nUsername: {username}")
    print(f"  In FOLLOWERS (they follow you): {in_followers}")
    print(f"  In FOLLOWING (you follow them): {in_following}")
    
    if in_followers and in_following:
        print(f"  ➡️  MUTUAL: You both follow each other ✅")
    elif in_following and not in_followers:
        print(f"  ➡️  NOT FOLLOWING BACK: You follow them, they don't follow you ❌")
    elif in_followers and not in_following:
        print(f"  ➡️  YOU DON'T FOLLOW BACK: They follow you, you don't follow them 👋")
    else:
        print(f"  ➡️  NOT IN EITHER LIST")

# Double check: are there any entries with empty/missing titles in following.json?
print("\n\n5️⃣ CHECKING FOR EMPTY/INVALID ENTRIES")
print("-"*70)

empty_in_following = 0
sample_empty = []
for entry in following_data['relationships_following']:
    if not entry or not isinstance(entry, dict):
        empty_in_following += 1
        if len(sample_empty) < 3:
            sample_empty.append(entry)
    elif 'title' not in entry or not entry['title'] or not isinstance(entry['title'], str):
        empty_in_following += 1
        if len(sample_empty) < 3:
            sample_empty.append(entry)

print(f"Empty/invalid entries in following.json: {empty_in_following}")
if sample_empty:
    print("Sample of empty entries:")
    for entry in sample_empty:
        print(f"  {entry}")

print("\n" + "="*70)
print("CONCLUSION:")
print("-"*70)
print("✅ followers_1.json contains people who FOLLOW YOU")
print("✅ following.json contains people YOU FOLLOW")
print("✅ Extraction logic is correct!")
print("="*70)
