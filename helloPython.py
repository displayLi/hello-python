#coding=utf-8
strings = 'hello world'
print (type(strings))

boos = True

print (type(boos))

# 让我去二
abc = ['qwer','rewqr',4]

print(type(abc))

data = {}

print(type(data))

datas = ()
print (type(datas))

a = 1
print (type(a))

b = 1.111
print (type(b))

def abc(a,b):
    print(a+b);

print(type(abc(1,1)))

class Pson:
    def btn(self):
        self.name = self

print (type(Pson))

fn = Pson

print(fn)