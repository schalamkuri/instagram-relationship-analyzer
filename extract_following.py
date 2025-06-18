#!/usr/bin/env python3
"""
Script to extract all usernames from Instagram following JSON file.
"""

import json
import os

def extract_usernames_from_following(json_file_path):
    """
    Extract all usernames from the following JSON file.
    
    Args:
        json_file_path (str): Path to the following JSON file
        
    Returns:
        list: List of usernames
    """
    usernames = []
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        # Check if relationships_following exists in the data
        if 'relationships_following' in data:
            # Iterate through each entry in the relationships_following array
            for entry in data['relationships_following']:
                # Check if string_list_data exists and is not empty
                if 'string_list_data' in entry and entry['string_list_data']:
                    # Extract the value (username) from each item in string_list_data
                    for string_data in entry['string_list_data']:
                        if 'value' in string_data:
                            usernames.append(string_data['value'])
        else:
            print("Error: 'relationships_following' key not found in the JSON file.")
            return []
                        
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file_path}'.")
        return []
    except Exception as e:
        print(f"Error processing file: {e}")
        return []
    
    return usernames

def save_usernames_to_file(usernames, output_file_path):
    """
    Save the list of usernames to a text file.
    
    Args:
        usernames (list): List of usernames
        output_file_path (str): Path to save the usernames
    """
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for username in usernames:
                file.write(f"{username}\n")
        print(f"Usernames saved to '{output_file_path}'")
    except Exception as e:
        print(f"Error saving usernames: {e}")

def main():
    # Path to your following JSON file
    json_file_path = "following.json"
    
    # Extract usernames
    print("Extracting usernames from following file...")
    usernames = extract_usernames_from_following(json_file_path)
    
    if usernames:
        print(f"Found {len(usernames)} accounts you're following!")
        
        # Display first 10 usernames as preview
        print("\nFirst 10 usernames:")
        for i, username in enumerate(usernames[:10], 1):
            print(f"{i}. {username}")
        
        if len(usernames) > 10:
            print(f"... and {len(usernames) - 10} more")
        
        # Save to file
        output_file = "following_usernames.txt"
        save_usernames_to_file(usernames, output_file)
        
        # Optional: Save as JSON for further processing
        json_output_file = "following_usernames.json"
        try:
            with open(json_output_file, 'w', encoding='utf-8') as file:
                json.dump(usernames, file, indent=2, ensure_ascii=False)
            print(f"Usernames also saved as JSON to '{json_output_file}'")
        except Exception as e:
            print(f"Error saving JSON file: {e}")
            
    else:
        print("No usernames found or error occurred.")

if __name__ == "__main__":
    main()
