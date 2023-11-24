# Create, Fill and draw an Histogram which reproduces the
# counts of a scaler linked to a Geiger counter.

import ROOT
hist = ROOT.TH1D("count_rate", "Count Rate;N_{Counts};# occurrences",\
                 # Number of Bins, Lower X Boundary, Upper X Boundary \
                 16, -0.5, 15.5)

mean_count=3.6
nmeas = 400

for i in range(nmeas):
    counts = ROOT.gRandom.Poisson(mean_count)
    hist.Fill(counts)

hist.Draw()

# Print summary
print ("Moments of Distribution:"\
       "\n - Mean     = ", hist.GetMean(), " +- ", hist.GetMeanError(),\
       "\n - Std Dev  = ", hist.GetStdDev(), " +- ", hist.GetStdDevError(),\
       "\n - Skewness = ", hist.GetSkewness(),\
       "\n - Kurtosis = ", hist.GetKurtosis())
