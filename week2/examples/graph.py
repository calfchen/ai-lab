import snap

''' Graph (Creation) '''

G1 = snap.TNGraph.New()       # Create empty directed graph

G1.AddNode(1)                 # Important: Add nodes before adding edges
G1.AddNode(5)
G1.AddNode(12)

G1.AddEdge(1, 5)              # Add edges
G1.AddEdge(5, 1)
G1.AddEdge(5, 12)

G2 = snap.TUNGraph.New()      # Create empty undirected graph

N1 = snap.TNEANet.New()       # Create empty multigraph with attributes

''' Graph (Traversal) '''

for NI in G1.Nodes():         # Node traversal
  print 'node id %d, out-degree %d, in-degree %d' % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())

for EI in G1.Edges():         # Edge traversal
  print '(%d, %d)' % (EI.GetSrcNId(), EI.GetDstNId())
  
for NI in G1.Nodes():         # Edge traversal by node
  for DstNId in NI.GetOutEdges():
    print '(%d, %d)' % (NI.GetId(), DstNId)

''' Graph (Saving & Loading) '''

# Save graph to text file
snap.SaveEdgeList(G1, 'test.txt', 'List of Edges')    

# Load graph from text file
G3 = snap.LoadEdgeList(snap.PNGraph, 'test.txt', 0, 1)

# Save graph to binary
FOut = snap.TFOut('test.graph')
G1.Save(FOut)
FOut.Flush()

# Load graph from binary
FIn = snap.TFIn('test.graph')
G4 = snap.TNGraph.Load(FIn)
