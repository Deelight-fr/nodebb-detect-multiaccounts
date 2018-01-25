import argparse
import csv
import requests
import json
import re

url = 'https://my.web.site/api/user/'
auht_cookie = 'change_me'

ip_dict = {}

def main(files):

    counter = 0

    for f in files:
        userReader = csv.reader(open(f, newline=''), delimiter=',')
        for row in userReader:
            counter += 1

            username = row[1]

            # replace ' ' and '.' with '-' in url
            api_friendly_username = re.sub(r'[ .]', '-', username)

            print("Analysing account #" + str(counter) + ":", api_friendly_username, "...")

            r1 = requests.get(url + api_friendly_username,
                cookies={'express.sid':auth_cookie})

            try:
                user_data = json.loads(r1.content)
            except ValueError:  # includes simplejson.decoder.JSONDecodeError
                print('Decoding JSON has failed :', r1.content)
                continue

            # Dont't check banned accounts
            if user_data['banned'] == False:
                user_ips = user_data['ips']
    
                for user_ip in user_ips:
                    if user_ip not in ip_dict:
                        ip_dict[user_ip] = []
                    ip_dict[user_ip].append(username);
            
    print()

    for user_ip, usernames in ip_dict.items():
        if len(usernames) > 1:
            print(user_ip, "matches: ", ', '.join(usernames))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs=1, help='path to the file')
    args_namespace = parser.parse_args()
    args = vars(args_namespace)['file']
    main(args)
