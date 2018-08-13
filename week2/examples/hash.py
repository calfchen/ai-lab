import snap

h = snap.TIntStrH()           # Create an empty table

h[5] = 'apple'                # Add elements
h[3] = 'tomato'
h[9] = 'orange'
h[6] = 'banana'
h[1] = 'apricot'

print h.Len()                 # Print table size

print 'h[3] = ', h[3]         # Get element value

h[3] = 'peach'                # Set element value
print 'h[3] =', h[3]

for key in h:                 # Iterate over keys
  print key, h[key]