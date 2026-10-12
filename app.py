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
        exit()
    elif opt == '3':
        print('git add . will add all changes to the staging area.')
        exit()
    elif opt == '4':
        print(f'Commit via: git commit -m "Your commit message here"')
        exit()
    elif opt == '5':
        print('Pushing changes to remote repository via:')
        print('if 1st time: gh repo create Git_Workflow_CLI --public')
        print('if link needed: git remote add origin https://github.com/randyscott777/Git_Workflow_CLI.git')
        print('to push changes to the remote repository: git push origin main')
        exit()
    elif opt == '6':
        print('Pulling changes from remote repository...')
        exit()
    else:
        print('Invalid choice. Please try again.')  
    print()

