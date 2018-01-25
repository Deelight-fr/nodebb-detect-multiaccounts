Detects NodeBB account which have been used from the same IP addresses.
Works remotely.

# Configuration

Set NodeBB website url
Set admin auth_cookie

(Auth cookie value can be obtained with a browser using developer mode. Its name is "express.sid")

# Usage

Export userlist as CSV through admin interface
python3 detect.py <users.csv>

# Notes

Will take some time
Will make one API request per user

# Todo

Some characters in usernames are not filtered yet. Ouputs "Decoding JSON has failed" but doesn't stop the script (account is ignored)
