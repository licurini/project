import requests

commitnumber = int(input("Write number of commits: "))

def get_commits(commit_num, num_on_page, page_num):
    commit = requests.get("https://api.github.com/repos/freeCodeCamp/freeCodeCamp/commits?per_page=100;page=(%d)" % page_num) 
    commit_list = []
    if commit_num > num_on_page:
        commit += get_commits(commit_num - num_on_page, num_on_page, page_num + 1)
    
    commit = commit.json()
    commit_list += commit
    


get_commits(commitnumber, 100, 1)

#print("SHA: " + commit_list[0]['sha'])
#print("Message: " + commit_list[0]['commit']['message'])
#print("URL: " + commit_list[0]['url'])