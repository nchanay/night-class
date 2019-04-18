# scope.property
x = 'global'

def f():
    # global x # this declares we are working with the global x and can be modified
    x = 'enclosed'
    print('in f', x)

    def  g():
        x = 'local'
        print('in g', x)

    g()

print(x)
f()
# print(g()) g is only in the scope of f
