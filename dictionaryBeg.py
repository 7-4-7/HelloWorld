"""DIXTIONARY
1.Ordered
2.Changeable/Mutable
3.No duplicates
                  |-------------item-----------|
4.stores data in {key              :       value} pair
                immuatble DT               no constraints"""
                #sets cant be used
#imutable=[int,float,tuple,True,strings]
nari={"name":"bha","college":"IIT","est":1978}
print(nari)

"Acessing values"

nari={"name":"bha","college":"IIT","est":1978}
print(nari["est"])

"Acessing keys"
for i in nari:
    print(i," ",end="")

"Duplicates"

"1.KEYS:final occurence overitws prev one"
nari={"name":"bha","college":"IIT","est":1978,"est":87}
print(nari)

"2.VALUES:no effect"
nari={"name":"bha","college":"IIT","est":87,"blue":87}
print(nari)




"LENGTH"
print(len(nari))

"type()"
print(type(nari))



"constructor dict"

nari=dict(name="Bharat",col="IIT",grad_year="2016")
print(nari)
nari=dict({"name":"Bharat",1:"IIT","grad_year":"2016"})
print(nari)

print()
print()
temp_ref=dict([(1,"one"),(True,"val"),((1,2,3),17093.3)])
print(temp_ref)#Key Duplicates dne 

temp_ref={1:"hello",True:"BHARAT"}
print(temp_ref)




"ASSIGINING"
ref[(1,True)]=123
print(ref)



"ACCSESSING ITEMS"
 #d[key]
ref={"name":"bha","college":"IIT","est":1978}
x=ref["name"]
print(x)
 #d.get(key)
print(ref.get("name"))


 #d.keys():return all keys of dictionary in [] type
x=list(ref.key())
print(x)
#d.values():return list of values
#items():return list of tuples
c=dict(ref.item())#can also be used for copying
print(c)
d={(1,2,3):"NUMBERS",
    True:23.0,
    False:-10,
    "word":("art","fire_place")}
print(d)






