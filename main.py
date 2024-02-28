if __name__ == '__main__':
    aliens = []
    for alien_number in range(30):
        new_alien = {'color': 'green', 'speed': 'fast', 'points': 7, 'number': alien_number}
        aliens.append(new_alien)
    for alien in aliens[:5]:
        print(alien)
    print('...')
    print(f'Total amount of aliens is {len(aliens)}')
