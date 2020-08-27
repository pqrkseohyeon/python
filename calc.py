def add(a,b):
    return a+b
def mul(a,b):
    return a*b

if __name__=='__main__': # 현재 파일을 실행하면 되고
    print(add(10,20))    # 모듈로 불러오면 실행안됨
    print(mul(10,20))