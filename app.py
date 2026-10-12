while True:
    print('1. init - initialize using Git')
    print('2. status - show current Git status')
    print('3. add - add changes to staging area')
    print('4. commit - commit changes with a message')
    print('5. push - push changes to remote repository')
    print('6. pull - pull changes from remote repository')

    opt = input('Enter your choice: ')
    if opt == '1':
        print('Initializing Git via: git init')
        print('and then do: git status')
        exit()
    elif opt == '2':
        print('Showing current Git status...')
    elif opt == '3':
        print('Adding changes to staging area...')
    elif opt == '4':
        message = input('Enter commit message: ')
        print(f'Committing changes with message: {message}')
    elif opt == '5':
        print('Pushing changes to remote repository...')
    elif opt == '6':
        print('Pulling changes from remote repository...')
    else:
        print('Invalid choice. Please try again.')  
    print()

