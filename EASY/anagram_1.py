"""Class Solution:

	def isanagram(self,s,t) :
		if len(s) != len(t):
			return False
		counts,countt={},{}

		for i in range(len(s)):
			counts[s[i]] = 1+ counts.get(s[i],0)
			countt[t[i]] = 1+ countt.get(t[i],0)
		for c in counts:
			if counts[c] != countt.get(c,0):
				return False
		return true

	print(isanagram('anagram','assd'))		
"""



def isanagram(s,t) :
	if len(s) != len(t):
		return False
	counts,countt={},{}

	for i in range(len(s)):
		counts[s[i]] = 1+ counts.get(s[i],0)
		print(counts)
		countt[t[i]] = 1+ countt.get(t[i],0)
		
	for c in counts:
		if counts[c] != countt.get(c,0):
			return False
	return True

print(isanagram('anagram','nagrama'))	


def isanagram2(s,t) :
	return sorted(s)==sorted(t)
print(isanagram2('anagram','nsagrama'))	


##print("Hello")