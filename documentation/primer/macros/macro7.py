# Draw a Bidimensional Histogram in many ways
# together with its profiles and projections

import ROOT

ROOT.gStyle.SetPalette(ROOT.kBird)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

h = ROOT.TH2D("bidi_h","2D Histo;Gaussian Vals;Exp. Vals", \
              30, -5, 5,  # X axis: nbis, low, high \ 
              30, 0, 10)  # Y axis: nbis, low, high

for i in range(500000):
    h.Fill(ROOT.gRandom.Gaus(0,2), 10 - ROOT.gRandom.Exp(4),.1)

c = ROOT.TCanvas("Canvas","Canvas",800,800)
c.Divide(2,2)
c.cd(1)
h.Draw("Cont1")
c.cd(2)
h.Draw("Colz")
c.cd(3)
h.Draw("Lego2")
c.cd(4)
h.Draw("Surf3")

# Profiles and Projections
c2 = ROOT.TCanvas("Canvas2","Canvas2",800,800)
c2.Divide(2,2)
c2.cd(1)
h.ProjectionX().Draw()
c2.cd(2)
h.ProjectionY().Draw()
c2.cd(3)
h.ProfileX().Draw()
c2.cd(4)
h.ProfileY().Draw()
