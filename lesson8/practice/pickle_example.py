import pickle


def foo():
    print('hello world')


data = [
    {
        'first_name': 'Tima',
        'last_name': 'Akulich'
    },
    {
        'first_name': 'John',
        'last_name': 'Doe',
        'foo': foo
    }
]

res = pickle.dumps(foo)
print(res)
# data = pickle.loads(res)
# print(data[1]['foo']())
