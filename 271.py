input = ["lint","code","love","you"]

encode_str = ""

for word in input:
    encode_str+=str(len(word))+"#"+word
print(encode_str)

decode_res, i =[],0

while i<len(encode_str):
    j=i
    while encode_str[j]!="#":
        j+=1
    length = int(encode_str[j-1])
    decode_res.append(encode_str[j+1:j+1+length])
    i=j+1+length
print(decode_res)




