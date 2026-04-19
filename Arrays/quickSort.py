
class QuickSort:
    def __init__(self, arr, low, high):
        self.arr = arr
        self.low = low
        self.high = high
    
    def Quick_Sort(self, arr, low, high):
        if low<high:
            pI=self.partition(arr,low,high)
            self.Quick_Sort(arr,low,pI-1)
            self.Quick_Sort(arr,pI+1,high)
        return arr

    def partition(self, arr, low, high):
        pivot = arr[low]
        i=low
        j=high
        while(i<j):
            while i<=high and pivot>=arr[i]:
                i+=1
            while j>=low and pivot<arr[j]:
                j-=1
            if(i<j):
                arr[i],arr[j]=arr[j],arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

if __name__ == "__main__":
    arr = [1,2,4,7,9,7,4,2,3,5]
    obj = QuickSort(arr, 0, len(arr)-1)    
    print(obj.Quick_Sort(arr, 0, len(arr)-1))
