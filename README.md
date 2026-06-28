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
- `excluded_accounts.txt` - Persistent list of usernames to omit from future comparisons

## 📊 What You'll Learn

The analysis shows you:

- **📈 Summary Statistics**: Total followers, following, mutual connections
- **✅ Mutual Followers**: People who follow you AND you follow them
- **❌ Not Following Back**: People you follow but they don't follow you
- **👥 You Don't Follow Back**: People who follow you but you don't follow them
- **📊 Percentages**: Mutual follow rates and other metrics

## 🚫 Excluding Ghost or Deactivated Accounts

If certain usernames show up in your non-mutual results but you know they are ghost, inactive, or deactivated accounts, add them to `excluded_accounts.txt` in the project root. The analyzer will subtract those usernames from future comparisons before calculating relationship counts.

The file accepts one username per line, and lines starting with `#` are ignored so you can leave notes in the list.

### Reference Finding

In the current report, 29 accounts in `not_following_back` were identified as likely ghost or deactivated accounts and added to the exclusion list. This is a starting point, not a permanent set. Review `excluded_accounts.txt` periodically and add more accounts as your network changes over time.

## 🧹 Post-Analysis Cleanup

After the report finishes, the analyzer now offers an optional cleanup prompt. If you accept it, the script removes the raw export files and generated analysis outputs so the workspace stays lightweight. The exclusion list is kept in place so your saved ghost/deactivated accounts continue to apply on the next run.

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

---

**Note**: This tool only processes data from Instagram's official export feature. It does not access Instagram directly or violate any terms of service.
