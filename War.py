Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import Counter
war_and_piece=('a' 'aa' 'abC' 'aa' 'ac' 'abc' 'bcd' 'a')
cnt = Counter()
for word in war_and_piece:
  cnt[word]+=1
print(cnt)  
