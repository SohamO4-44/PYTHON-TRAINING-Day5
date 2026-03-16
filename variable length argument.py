mylist=[5,2,9,7,5,6]
def searchElements(target):
 for i in range(len(mylist )):
    if target == mylist[i]:
     print("element found at index number=",i)
searchElements(7)
