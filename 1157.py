def alpha(str):
    dict = {x:0 for x in str}
    for n in str:
        dict[n] = dict[n] + 1

    m = max(dict.values())
    m_key = [k for k,v in dict.items() if v == m]

    if len(m_key) == 1:
        return m_key[0]
    return '?'


if __name__ == '__main__':
    str = input().upper()
    print(alpha(str))
