print("reastaurant management")
k=input("Enter your login key: ")
c="rvbv**29sana"
if k!=(c):
    print("your password is incorrect")
else:
    print("you are logged in")
s=input("show menu (y/n): ")
menu=("cpca cola","lemon lime drink","pepsi","sprite")
if s=='y':
    for i in menu:
        print(i)
    d=input("enter your order please: ")
    order="mountain dew","crush" 
    if d!=(order):
        print("not available")
    else:
        print("order placed")
else:
    print("bye")
