if __name__ == '__main__':
    responses = {}
    poll_is_active = True
    while poll_is_active:
        name = input('\nWhat is your name? ')
        response = input('Which mountain would you like to climb? ')
        responses[name] = response
        repeat = input('Would you like to let another person respond? (yes/no) ')
        if repeat == 'no':
            poll_is_active = False
    print('\n---Poll results---')
    for name, response in responses.items():
        print(f'{name} would like to climb {response} mountain.')
