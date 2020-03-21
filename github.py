import requests


#commitnumber = input("Write number of commits: ")

commit = requests.get("https://api.github.com/repos/freeCodeCamp/freeCodeCamp/commits?per_page=1")
commit_json = commit.json()

print("SHA: " + commit_json[0]['sha'])
print("Message: " + commit_json[0]['commit']['message'])
print("URL: " + commit_json[0]['url'])