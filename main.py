if __name__ == '__main__':
    favourite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell']
    }
    for name, languages in favourite_languages.items():
        print(f'\n{name.title()}\'s favourite language are:', end=' ')
        for language in languages:
            print(f'{language.title()}', end=' ')
