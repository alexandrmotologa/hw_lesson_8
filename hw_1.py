users = [
    {
        'name': 'Johny',
        'email': 'j@g.com',
        'rating': 3.5 
    },
    {
        'name': 'Ivan',
        'email': 'iii@g.com',
        'rating': 4.5 
    },
    {
        'name': 'Maary',
        'email': 'mar@g.com',
        'rating': 4.0 
    },
    {
        'name': 'Vaniuha',
        'email': 'van@g.com',
        'rating': 2.1 
    },
    {
        'name': 'Zuck',
        'email': 'zuck@g.com',
        'rating': 5.0 
    },
    {
        'name': 'Snow',
        'email': 'snow@g.com',
        'rating': 4.1
    }
    
]

def swap(i):
    name_swap = users[i]
    users[i] = users[i+1]
    users[i+1] = name_swap
    # for u in users:
    #     print(" >> ", u['name'])
    # doar schimbarea name(i)(+1) fara afisare :D

swap(4)