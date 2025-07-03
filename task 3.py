v1='Savio falcone'
v2=0.0091
v3=5
v4="true"
v5=5+4j
 
 #---------------types---------------------
print("v1:", v1, "Type:", type(v1))
print("v2:", v2, "Type:", type(v2))
print("v3:", v3, "Type:", type(v3))
print("v4:", v4, "Type:", type(v4))
print("v5:", v5, "Type:", type(v5))

#-----------------conversion_---------------------------
# Convert each to another simple data type
v1_new = str(v1)        # stays as str
v2_new = int(v2)        # float to int
v3_new = float(v3)      # int to float
v4_new = bool(v4)       # non-empty string to True
v5_new = str(v5)        # complex to string

#-------------new one-------------------
# Print converted values and types
print("v1:", v1_new, "Type:", type(v1_new))
print("v2:", v2_new, "Type:", type(v2_new))
print("v3:", v3_new, "Type:", type(v3_new))
print("v4:", v4_new, "Type:", type(v4_new))
print("v5:", v5_new, "Type:", type(v5_new))
