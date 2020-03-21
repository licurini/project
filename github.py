import requests


#commitnumber = input("Write number of commits: ")
#print(commitnumber)

commitlist = requests.get("https://api.github.com/repos/freeCodeCamp/freeCodeCamp/commits?per_page=1")
commited = commitlist.json()

print(commited[0]['sha'])