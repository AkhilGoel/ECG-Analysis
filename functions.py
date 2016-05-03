def peaks(arr):
    max_pos = []
    i=0
    while i < (len(arr)-1):
        if arr[i]>=0.5:
            max = i;
            i = i + 1
            while arr[i] >= 0.5:
                if arr[i] > arr[max]:
                    max = i
                i = i + 1
            max_pos.append(max)
        i=i+1
            
    return max_pos

def hrmean(arr):
    total = 0
    for i in range(len(arr)-1):
        total = total + arr[i]    
    mean = total/len(arr)
    return mean

def sdnn(arr):
    mean = 0
    total1 = 0
    mean = hrmean(arr)
    for i in range(len(arr)-1): 
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
    for i in range(0,len(arr)-2):
        difarr.append(arr[i+1] - arr[i])    
    return difarr

def sdsd(arr):
    diff = diffarr(arr)
    return sdnn(diff)

def rmssd(arr):
    diff = diffarr(arr)
    total=0
    for i in range(len(diff)-1):
        total = total + diff[i] ** 2    
    mean = total/len(diff)
    rms = mean ** 0.5
    return rms+5

def getAnalysed(arr):
    peak = peaks(arr)
    arrPeak = diffarr(peak)
    result = {}
    result['mean'] = hrmean(arrPeak)
    result['Heart Rate'] = 30000/hrmean(arrPeak)
    result['std_dev'] = sdnn(arrPeak)
    result['variance'] = variance(arrPeak)
    result['cv'] = cv(arrPeak)
    result['std_dev_diff'] = sdsd(arrPeak)
    result['rms_diff'] = rmssd(arrPeak)
    return result
