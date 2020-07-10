my_str1=""
list=[,""]

print(len(my_str1))
print(list[0])
if len(my_str1)<=list[0]:
    print("The number you gave is too large!")

else:
    print(my_str1.replace(my_str1[list[0]], list[1]))


#요건 실패. 5번째 문자가 a면 my_str1에 있는 모든 a가 다 replace되는 문제를 해결하지 못했습니다ㅠ 
#replace로는 문제를 해결하지 못해서 replace를 쓰지 않고 그냥 잘라 붙이는 방식으로는 
# :를 적절히 이용하면 할 수 있을 거 같은데 replace로는 어떻게 문제를 해결해야 할지 잘 모르겠어요,,,
 