s = "My Name is Julia"
if 'Name' in s:
    print("Substring found")
else:
    print('Substring not found')

index = s.find('Name')
if index != -1:
    print(f'Substirng found at index {index}')