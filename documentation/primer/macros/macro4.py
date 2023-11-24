# Create, Draw and fit a TGraph2DErrors

import ROOT
from array import array

ROOT.gStyle.SetPalette(ROOT.kBird)
e = 0.3
nd = 500

f2 = ROOT.TF2("f2", "1000*(([0]*sin(x)/x)*([1]*sin(y)/y))+200",\
              -6,6,-6,6)
f2.SetParameters(1,1)
dte = ROOT.TGraph2DErrors(nd)

# Fill the 2D graph
x = array('d', [0.0])
y = array('d', [0.0])
for i in range(nd):
    f2.GetRandom2(x,y)
    # A random number in [-e,e]
    rnd = ROOT.gRandom.Uniform(-e,e)
    z = f2.Eval(x[0],y[0])*(1+rnd)
    dte.SetPoint(i,x[0],y[0],z)
    ex = 0.05*ROOT.gRandom.Uniform()
    ey = 0.05*ROOT.gRandom.Uniform()
    ez = abs(z*rnd)
    dte.SetPointError(i,ex,ey,ez)

# Fit function to generated data
f2.SetParameters(0.7,1.5)  # set initial values for fit
f2.SetTitle("Fitted 2D function")
dte.Fit(f2)

# Plot the result
c1 = ROOT.TCanvas()
f2.SetLineWidth(1)
f2.SetLineColor(ROOT.kBlue-5)
f2.Draw("Surf1")
f2.GetXaxis().SetTitle("X Title")
f2.GetYaxis().SetTitle("Y Title")
f2.GetZaxis().SetTitle("Z Title")
f2.GetXaxis().SetTitleOffset(1.5)
f2.GetYaxis().SetTitleOffset(1.5)
f2.GetZaxis().SetTitleOffset(1.5)
dte.Draw("P0 Same")

# Make the x and y projections on extra canvas
c_p = ROOT.TCanvas("ProjCan", "The Projections",1000,400)
c_p.Divide(2,1)
c_p.cd(1)
dte.Project("x").Draw()
c_p.cd(2)
dte.Project("y").Draw()
