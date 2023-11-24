# Divide and add 1D Histograms

import ROOT

def format_h(h, linecolor):
    h.SetLineWidth(3)
    h.SetLineColor(linecolor)

sig_h = ROOT.TH1D("sig_h","Signal Histo",50,0,10)
bkg_h = ROOT.TH1D("exp_h","Exponential Histo",50,0,10)

# simulate the measurements
for imeas in range(10000):
    bkg_h.Fill(ROOT.gRandom.Exp(4))
    if imeas%10==0: sig_h.Fill(ROOT.gRandom.Gaus(5,.5))

for col, hist in enumerate([sig_h,bkg_h]):
    format_h(hist, col+1)

# Add and Divide
sum_h = bkg_h.Clone("sum")
sum_h.Add(sig_h, 1.)

ratio = sig_h.Clone("ratio")
ratio.Divide(bkg_h)

# Draw and format
ROOT.gStyle.SetOptStat(0)
c = ROOT.TCanvas("c", "c", 600, 800)
c.Divide(1,2)
c.cd(1)
sum_h.Draw("hist")
bkg_h.Draw("SameHist")
sig_h.Draw("SameHist")
format_h(sum_h,ROOT.kBlue)
sum_h.SetTitle("Exponential + Signal")
sum_h.GetXaxis().SetTitle("X")
sum_h.GetYaxis().SetTitle("N")

c.cd(2)
ratio.Draw()
ratio.SetTitle("S/B Ratio")
format_h(ratio, ROOT.kOrange)
ratio.GetXaxis().SetTitle("X")
ratio.GetYaxis().SetTitle("Ratio")
