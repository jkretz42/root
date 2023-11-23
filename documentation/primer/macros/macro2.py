# Reads expected/measured points from a file and produces an overlay of two graphs
import ROOT

c = ROOT.TCanvas()
c.SetGrid()
    
graph1 = ROOT.TGraphErrors("macro2_input_expected.txt", "%lg %lg %lg")
graph1.SetTitle("Measurement XYZ and Expectation;length [cm];Arb.Units")
graph1.SetFillColor(ROOT.kYellow)
graph1.Draw("E3AL") # E3 draws the band

graph2 = ROOT.TGraphErrors("./macro2_input.txt","%lg %lg %lg")
graph2.SetMarkerStyle(ROOT.kCircle);
graph2.SetFillColor(0)
graph2.Draw("PESame")

# Draw the Legend
leg = ROOT.TLegend(.1,.7,.3,.9,"Lab. Lesson 2")
leg.SetFillColor(0)
leg.AddEntry(graph1,"Expected Points")
leg.AddEntry(graph2,"Measured Points")
leg.Draw("Same")

graph2.Print()
