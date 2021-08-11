#print ('_'.join(input().split()))
import re
print(re.sub(r'\s+', '_', re.sub(r'^\s+(.+?)\s+$', r'\1', input())))
