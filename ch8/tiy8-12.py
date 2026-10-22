def make_sandwich(*items):
    print('\nYou are ordering a sandwich with the following ingredients:')
    for item in items:
        print(f'- {item}')

make_sandwich('tomatoe', 'garlic', 'ham')
make_sandwich('lettuce', 'ketchup', 'chicken', 'tomatoe')
make_sandwich('ham')
