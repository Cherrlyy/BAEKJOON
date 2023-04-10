from collections import Counter
import math

def room_num(n):
    dic = dict(Counter(n))
    m = 0
    for key in dic:
        if key not in ('6', '9'):
            m = max(dic.get(key, 0), m)

    m = max(int(math.ceil((dic.get('6', 0)+dic.get('9', 0))/2)), m)
    return m

if __name__ == '__main__':
    n = input()
    print(room_num(n))
