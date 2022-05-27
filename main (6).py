# Shell sort implementation 
def shellsort(alist):
  gap = len(alist) // 2
  while gap > 0:
    for index in range(gap,len(alist)):
      current_element = alist[index]
      pos = index
      while pos >= gap and current_element < alist[pos - gap]:
        alist[pos] = alist[pos - gap]
        pos = pos -gap 
      alist[pos] = current_element
    gap = gap // 2

n = int(input("list length:"))
list1 = [int(input(f"enter element {x}:")) for x in range(n)]
shellsort(list1)
print(list1)
    
