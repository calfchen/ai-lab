import snap

v = snap.TIntV()              # Create an empty vector

v.Add(1)                      # Add elements
v.Add(2)
v.Add(3)
v.Add(4)
v.Add(5)

print v.Len()                 # Print vector size

print v[3]                    # Get & Set elements
v[3] = 2*v[2]
print v[3]

for item in v:                # Iterate over elements
  print item
  
for i in range(0, v.Len()):
  print i, v[i]