users = [
    {'name': 'Johny', 'email': 'j@g.com', 'rating': 3.5},
    {'name': 'Ivan', 'email': 'iii@g.com', 'rating': 4.5},
    {'name': 'Maary', 'email': 'mar@g.com', 'rating': 4.0},
    {'name': 'Vaniuha', 'email': 'van@g.com', 'rating': 2.1},
    {'name': 'Zuck', 'email': 'zuck@g.com', 'rating': 5.0},
    {'name': 'Snow', 'email': 'snow@g.com', 'rating': 4.1},
    ]


def display():
    for u in users:
        print (' >> ', u['name'])


def bubble_sort(ascending=False):
    if ascending == False:
        for j in range(len(users)):
            for i in range(len(users) - 1):
                if users[i]['rating'] < users[i + 1]['rating']:
                    temp = users[i]
                    users[i] = users[i + 1]
                    users[i + 1] = temp
    else:
        for j in range(len(users)):
            for i in range(len(users) - 1):
                if users[i]['rating'] > users[i + 1]['rating']:
                    temp = users[i]
                    users[i] = users[i + 1]
                    users[i + 1] = temp
    display()


bubble_sort(True)
