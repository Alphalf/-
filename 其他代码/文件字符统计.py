# Write your code here :-)
print(Counter(re.findall(r'\w+',open('Personal data.db.log').read().lower())))
