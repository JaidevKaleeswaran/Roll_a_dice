import random

response = input("Do you want to roll a dice?: ")
while(response == 'y'):
    no = random.randint(0, 6)
    print('[-----]')
    if(no == 1):
        print('[     ]')
        print('[  0  ]')
        print('[     ]')
    elif(no == 2):
        print('[     ]')
        print('[0   0]')
        print('[     ]')
    elif(no == 3):
        print('[     ]')
        print('[0 0 0]')
        print('[     ]')
    elif(no == 4):
        print('[0   0]')
        print('[     ]')
        print('[0   0]')
    elif(no == 5):
        print('[0   0]')
        print('[  0  ]')
        print('[0   0]')
    else:
        print('[0   0]')
        print('[0   0]')
        print('[0   0]')
    print('[-----]')
    response = input('press y to roll again and n to exit: ')

    if response == 'n':
        exit()
    else: 
        while response != 'y' and response != 'n':
            response = input('press y to roll again and n to exit: ')