import time

#단순 숫자 증가
start = time.time()
t = 0
for i in range(10000):
    t = t+1
print(t)

end = time.time()

print(f"{end - start:.10f} sec")


# 리스트 추가 후 갯수 세기
start = time.time()
t = []
for i in range(10000):
    t.append(i)
print(len(t))

end = time.time()

print(f"{end - start:.10f} sec")