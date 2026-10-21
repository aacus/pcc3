def make_shirt(size='large', text='I love Python'):
    msg = f'We will print a {size} sized shirt with the following text: {text}'
    print(msg)

make_shirt()
make_shirt('medium')
make_shirt('small', 'I dont love Python')