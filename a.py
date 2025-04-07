import json
import os
os.system('clear')
with open ('users_100.json', 'r') as fa:
    out= json.load (fa)
    for f in out:
        print("id: {}".format(f["id"])) 
        print("name: {}".format(f["name"]))
        print("city :{}".format(f["city"]))
        print("age :{}".format(f["age"]))
        print("friends :")
        for friend in f["friends"]:
            print("   - {} (Hobbies: {})".format(friend["name"], ", ".join(friend["hobbies"])))
        input()
