import ROOT
from array import array # needed to pass arrays to PyROOT

# The values and the errors on the Y axis
x_vals = array('d', [1,2,3,4,5,6,7,8,9,10])
y_vals = array('d', [6,12,14,20,22,24,35,45,44,53])
y_errs = array('d', [5,5,4.7,4.5,4.2,5.1,2.9,4.1,4.8,5.43])

# create graph with errors
graph = ROOT.TGraphErrors(len(x_vals), x_vals, y_vals, ROOT.nullptr, y_errs)
graph.SetTitle("Measurement XYZ;length [cm];Arb.Units")

# format the plot
graph.SetMarkerStyle(ROOT.kOpenCircle)
graph.SetMarkerColor(ROOT.kBlue)
graph.SetLineColor(ROOT.kBlue)

# The canvas on which we'll draw the graph
mycanvas = ROOT.TCanvas("c", "c", 0, 0, 800, 600)

# Draw the graph
graph.Draw("APE")

# Define a linear function
f = ROOT.TF1("Linear law","[0]+x*[1]",.5,10.5)

# format the line
f.SetLineColor(ROOT.kRed)
f.SetLineStyle(2)

# Fit it to the graph and draw it
graph.Fit(f)
f.Draw("same")

# Build and Draw a legend
leg = ROOT.TLegend(.1,.7,.3,.9,"Lab. Lesson 1")
leg.SetFillColor(0)
graph.SetFillColor(0)
leg.AddEntry(graph,"Exp. Points")
leg.AddEntry(f,"Th. Law")
leg.Draw("same")

# Draw an arrow on the canvas
arrow = ROOT.TArrow(8,8,6.2,23,0.02,"|>")
arrow.SetLineWidth(2)
arrow.Draw()

# Add some text to the plot
text = ROOT.TLatex(8.2,7.5,"#splitline{Maximum}{Deviation}")
text.Draw()

mycanvas.Print("graph_with_law.pdf")

