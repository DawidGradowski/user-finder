import datetime

users = {}


def main():
    global users
    users = read_users("users.txt")
    user = input("Input user name and number (Jan_Kowalski-111222333): ")
    start_time = datetime.datetime.now()
    users.sort()
    if find(user) is not False:
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
    min_index = 0
    max_index = len(users) - 1
    mid_index = int(len(users) / 2)
    while True:
        if users[mid_index] == user:
            return True
        elif users[mid_index] > user:
            max_index = mid_index - 1
        elif users[mid_index] < user:
            min_index = mid_index + 1
        mid_index = int((max_index + min_index) / 2)
        if max_index == min_index:
            return False


main()
