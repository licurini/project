import requests

commitnumber = int(input("Write number of commits: "))

def get_commits(commit_num, num_on_page, page_num):
    commit = requests.get("https://api.github.com/repos/freeCodeCamp/freeCodeCamp/commits?per_page=100;page=(%d)" % page_num).json()
    commit_list = commit
    if commit_num > num_on_page:
        commit_num = commit_num - num_on_page
        page_num += 1
        commit_list += get_commits(commit_num, num_on_page, page_num)
        print(commit)
    
    i = 0
    while i < commit_num:
        print(i + 1)
        print("SHA: " + commit_list[i]['sha'])
        print("Message: " + commit_list[i]['commit']['message'])
        print("URL: " + commit_list[i]['url'] + "\n" + 20 * "=")
        i += 1

get_commits(commitnumber, 100, 1)

