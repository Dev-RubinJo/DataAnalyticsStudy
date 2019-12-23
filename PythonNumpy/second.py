import numpy as np


## np.array함수로 array 생성
x = np.array([1, 2, 3, 4])
print(x)

y = np.array([[2, 3, 4], [1, 2, 5]])
print(y)

## np.arange함수로 array 생성
z = np.arange(10)
print(z)
a = np.arange(1, 10)
print(a)
b = np.arange(1, 10, 2)
print(b)
c = np.arange(5, 101, 5)
print(c)

## np.ones, np.zeros로 생성
d = np.ones((4, 5))
print(d)
e = np.zeros((2, 2, 3, 4))
print(e)

## np.empty, np.full로 생성
f = np.empty((3, 4))
print(f)

g = np.full((3, 4, 2), 7)
print(g)

## np.eye로 단위행렬 생성
h = np.eye(6)
print(h)

## np.linspace로 생성
i = np.linspace(1, 10, 3)
print(i)

j = np.linspace(1, 10, 4)
print(j)

## reshape 함수 사용
## ndarray의 형태, 차원을 바꾸기 위해 사용 -> reshape하려는 크기와 원소의 개수가 같아야한다.
x = np.arange(1, 16)
print(x)
x.shape

x = x.reshape(3, 5)
print(x)