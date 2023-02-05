import datetime

users = {}

def main():
    global users
    users = read_users("users.txt")
    user = input("Input user name and number (Jan_Kowalski-111222333): ")
    start_time = datetime.datetime.now()
    if find(user) is not None:
        print("User was found!")
    else:
        print("User wasn't found.")
    end_time = datetime.datetime.now()
    print(end_time - start_time)

def read_users(file):
    with open(file, "r") as f:
        lines = f.read()
        return lines.split("\n")

def find(user):
    global users
    for checked_user in users:
        if user == checked_user:
            return True

main()