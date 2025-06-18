#!/usr/bin/env python3
"""
Instagram Analyzer Cleanup Script
This script removes all generated files after running instagram_analyzer.py
to prepare for a fresh analysis.
"""

import os
import sys
from pathlib import Path

def cleanup_files():
    """Remove all generated files from Instagram analysis."""
    
    # List of files to delete (both input and output files)
    files_to_delete = [
        # Input files (Instagram JSON exports)
        "followers_1.json",
        "following.json",
        
        # Generated output files
        "followers_usernames.txt",
        "followers_usernames.json",
        "following_usernames.txt", 
        "following_usernames.json",
        "relationship_analysis.txt",
        "relationship_analysis.json"
    ]
    
    print("🧹 Instagram Analyzer Cleanup Script")
    print("=" * 50)
    print()
    
    deleted_count = 0
    not_found_count = 0
    
    for filename in files_to_delete:
        file_path = Path(filename)
        
        if file_path.exists():
            try:
                file_path.unlink()
                print(f"✅ Deleted: {filename}")
                deleted_count += 1
            except Exception as e:
                print(f"❌ Error deleting {filename}: {e}")
        else:
            print(f"ℹ️  Not found: {filename}")
            not_found_count += 1
    
    print()
    print("=" * 50)
    print("📊 CLEANUP SUMMARY:")
    print(f"   Files deleted: {deleted_count}")
    print(f"   Files not found: {not_found_count}")
    print(f"   Total files processed: {len(files_to_delete)}")
    
    if deleted_count > 0:
        print()
        print("✅ Cleanup complete! The workspace is now clean for future analysis.")
    else:
        print()
        print("ℹ️  No files were deleted. The workspace was already clean.")
    
    print("=" * 50)

def main():
    """Main function with confirmation prompt."""
    print("🧹 Instagram Analyzer Cleanup Script")
    print("=" * 50)
    print()
    print("This script will delete the following files:")
    print("• followers_1.json")
    print("• following.json")
    print("• followers_usernames.txt")
    print("• followers_usernames.json")
    print("• following_usernames.txt")
    print("• following_usernames.json")
    print("• relationship_analysis.txt")
    print("• relationship_analysis.json")
    print()
    
    # Ask for confirmation
    response = input("Are you sure you want to delete these files? (y/N): ").strip().lower()
    
    if response in ['y', 'yes']:
        print()
        cleanup_files()
    else:
        print()
        print("❌ Cleanup cancelled.")
        print("=" * 50)

if __name__ == "__main__":
    main()
