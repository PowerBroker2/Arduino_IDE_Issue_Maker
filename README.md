# Arduino_IDE_Issue_Maker
Python app to automatically create an issue to add a library to the Arduino IDE's Libraries Manager

# Example Batch File Usage:
'''
set /P id=Enter Repository Name:
python make_issue.py -u your_GitHub_username -t your_GitHub_personal_access_token -r %id%
PAUSE
'''
