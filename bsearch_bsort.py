#Bubble sort

alist=[]
b=input("Enter total number of integers:")
c=input("Enter {} numbers:".format(b))


# To take inputs in a list 
alist=c.split()	
num1=input("Enter new number:")
alist.append(num1)

for i in range(len(alist)):
    for j in range(len(alist)):
        if alist[i]>alist[j]:
            alist[i], alist[j] = alist[j], alist[i]


#Binary search

start=0
end=len(alist)-1


def bsearch(arr,start,end,num1):
	mid=int((start+end)/2)
	if arr[mid]==num1:
		return mid
	elif arr[mid]<num1:
		return bsearch(arr,start,mid-1,num1)
	else:
		return bsearch(arr,mid+1,end,num1)


result=bsearch(alist,start,end,num1)
print(alist)
print("The number is at {} position".format(result+1))

