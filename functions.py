def peaks(arr):
    max_pos = []
    for i in range(len(arr)):
        if arr[i]>=0.5:
            max = i;
            i = i + 1
            while arr[i] >= 0.5:
                if arr[i] > arr[max]:
                    max = i
                i = i + 1
            max_pos.append(max)

def hrmean(arr):
    total = 0
    for i in range(len(arr)):
        total = total + arr[i]    
    mean = total/len(arr)
    return mean

def sdnn(arr):
    mean = 0
    total1 = 0
    mean = hrmean(arr)
    for j in range(len(arr)): 
        v1 = (arr[i]-mean) ** 2
        total1 = total1 + v1
    std = (total1/len(arr)) ** 0.5
    return std

def variance(arr):
    Variance = sdnn(arr) ** 2
    return Variance

def cv(arr):
    cv = variance(arr)*100
    return cv

def diffarr(arr):
    difarr = []
    for i in range(len(arr)-1):
        diffarr[i] = arr[i+1] - arr[i]    
    return difarr

def sdsd(arr):
    diff = diffarr(arr)
    return sdnn(diff)

def rmssd(arr):
    diff = diffarr(arr)
    total=0
    for i in range(len(diff)):
        total = total + diff[i] ** 2    
    mean = total/len(diff)
    rms = mean ** 0.5
    return rms
