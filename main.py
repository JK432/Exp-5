# Write a Python program to create a list of strings. Separate palindromes in the list to another list using reverse() function
lst=["malayalam","leh","ladakh","ney"]
pallst=[]
for i in lst:
  srt=i
  srt="".join(reversed(srt))
  if srt==i:
    pallst.append(i)
print(pallst)