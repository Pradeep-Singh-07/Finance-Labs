a='80.85.51.70.75.77.75.83.74.73.50.72.83.83.83.55.71.52.90.84.77.88.90.86.80.69.90.86.69.78.66.84.80.69.52.70.54.77.50.76.71.66.70.72.87.84.75.66.74.74.87.72.69.52.68.68'
arr=a.split('.')
ans=''
for x in arr:
    ans+=chr(int(x))
print(ans)