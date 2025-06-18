# Instagram Relationship Analyzer

A comprehensive Python script to analyze your Instagram followers and following relationships using data from Instagram's official data export.

## 🚀 Quick Start

1. **Get your Instagram data export**:
   - Sign into [accountscenter.instagram.com](https://accountscenter.instagram.com)
   - Under Account settings → Your information and permissions → Download your information
   - Download or tranfer information → Pick the account you want → Some of your information → Under Connections, pick Followers and following → Download to device
   - Change date range to All time
   - Change Format to JSON
   - Hit Create files and wait for your data to download
   - It will take a few minutes, but you should be able to see and download the data in the 'Download your information' section
   - Extract the ZIP file and locate the `connections/followers_and_following/` folder

2. **Place your JSON files**:
   - Copy `followers_1.json` and `following.json` to the same directory as this script

3. **Run the analyzer**:
   ```bash
   python3 instagram_analyzer.py
   ```

## 📁 Output Files

The script generates the following files:

### Individual Username Lists:
- `followers_usernames.txt` - List of all your followers (one per line)
- `followers_usernames.json` - Same data in JSON format
- `following_usernames.txt` - List of all accounts you follow (one per line)  
- `following_usernames.json` - Same data in JSON format

### Relationship Analysis:
- `relationship_analysis.txt` - **Main analysis file** with comprehensive breakdown
- `relationship_analysis.json` - Same analysis in JSON format for programming

## 📊 What You'll Learn

The analysis shows you:

- **📈 Summary Statistics**: Total followers, following, mutual connections
- **✅ Mutual Followers**: People who follow you AND you follow them
- **❌ Not Following Back**: People you follow but they don't follow you
- **👥 You Don't Follow Back**: People who follow you but you don't follow them
- **📊 Percentages**: Mutual follow rates and other metrics

## 🔧 Individual Scripts

If you prefer to run parts separately, these scripts are also available:

- `extract_followers.py` - Extract only followers data
- `extract_following.py` - Extract only following data  
- `compare_relationships.py` - Compare existing extracted data

## 📋 Requirements

- Python 3.6+
- No external dependencies (uses only built-in libraries)

## 🛠️ Troubleshooting

**File not found errors**: 
- Make sure `followers_1.json` and `following.json` are in the same directory
- Check that the file names match exactly (Instagram sometimes uses different names)

**Empty results**:
- Verify your JSON files contain data (not empty or corrupted)
- Check that the JSON structure matches Instagram's current format

**Permission errors**:
- Make sure you have write permissions in the directory
- Try running from a different folder if needed

## 🧹 Cleanup

After running the analysis, you can clean up all generated files to prepare for a fresh analysis:

```bash
python3 cleanup.py
```

### What Gets Cleaned Up

The cleanup script removes:

**Input Files:**
- `followers_1.json` - Your Instagram followers export
- `following.json` - Your Instagram following export

**Generated Output Files:**
- `followers_usernames.txt` & `followers_usernames.json`
- `following_usernames.txt` & `following_usernames.json`  
- `relationship_analysis.txt` & `relationship_analysis.json`

### Features

- **Interactive confirmation** - Asks before deleting anything
- **Cross-platform compatibility** - Works on Windows, macOS, and Linux
- **Detailed feedback** - Shows exactly what was deleted
- **Safe operation** - Only removes known analysis files
- **Summary report** - Displays cleanup statistics

### Example Output

```
🧹 Instagram Analyzer Cleanup Script
==================================================

This script will delete the following files:
• followers_1.json
• following.json
• followers_usernames.txt
• followers_usernames.json
• following_usernames.txt
• following_usernames.json
• relationship_analysis.txt
• relationship_analysis.json

Are you sure you want to delete these files? (y/N): y

✅ Deleted: followers_1.json
✅ Deleted: following.json
✅ Deleted: followers_usernames.txt
✅ Deleted: followers_usernames.json
✅ Deleted: following_usernames.txt
✅ Deleted: following_usernames.json
✅ Deleted: relationship_analysis.txt
✅ Deleted: relationship_analysis.json

==================================================
📊 CLEANUP SUMMARY:
   Files deleted: 8
   Files not found: 0
   Total files processed: 8

✅ Cleanup complete! The workspace is now clean for future analysis.
==================================================
```

**💡 Tip**: Use the cleanup script between different Instagram data exports to ensure you're working with fresh data each time.

---

**Note**: This tool only processes data from Instagram's official export feature. It does not access Instagram directly or violate any terms of service.
