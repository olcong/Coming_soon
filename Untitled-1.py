x= int(input("x좌표를 입력하시요:"))
y= int(input("y좌표를 입력하시오:"))
if x>0 and y>0 :
    print("1사분면입니다")
elif x<0 and y>0:
    print("2사분면입니다")
elif x>0 and y>0:
    print("4사분면입니다")
elif x<0 and y<0 :
    print("3사분면입니다")
else :
    print("점이 y 혹은 x 선 혹은 원점 위에 있습니다")