import ROOT

ROOT.gROOT.SetStyle("Plain")   # set plain TStyle
ROOT.gStyle.SetOptStat(111111) # draw statistics on plots, 0 for no output
ROOT.gStyle.SetOptFit(1111)    # draw fit results on plot, 0 for no ouput
ROOT.gStyle.SetPalette(57)     # set color map
ROOT.gStyle.SetOptTitle(0)     # suppress title box

c1 = ROOT.TCanvas("c1","<Title>",0,0,400,300) # create a canvas, specify position and size in pixels
c1.Divide(2,2) # subdivide the canvas into 2x2 pads

f2 = ROOT.TF1("f2","[0]*sin([1]*x)/x",0.,10.)

c1.cd(1)       # change to pad 1 of canvas c1
f2.SetParameter(0,1)
f2.SetParameter(1,1)
f2.DrawCopy()

c1.cd(2)       # change to pad 2 of canvas c1
f2.SetParameter(0,1./2.)
f2.SetParameter(1,2)
f2.DrawCopy()

c1.cd(3)       # change to pad 3 of canvas c1
f2.SetParameter(0,1./3.)
f2.SetParameter(1,3)
f2.DrawCopy()

c1.cd(4)       # change to pad 4 of canvas c1
f2.SetParameter(0,1/4.)
f2.SetParameter(1,4)
f2.DrawCopy()

c1.SaveAs("test.pdf")
