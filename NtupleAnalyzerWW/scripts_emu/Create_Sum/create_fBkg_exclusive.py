from ROOT import RDataFrame, TFile, TChain, TTree, TH1D, TLorentzVector, TCanvas
import numpy
import sys
from math import cos, sin, sqrt, pi
import ROOT
import time as timer
ROOT.EnableImplicitMT()
year = sys.argv[1]
print("year is", year, "created fake bkg")

time_start = timer.time()
histnamelist = ["ptemu"]
MClist = ["VV","Top","ZTT"]
fdataSS = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/hSS_data.root".format(year),"read")
fout = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/h_Fake.root".format(year),"recreate")
for histname in histnamelist:
    hBKGOS = fdataSS.Get(histname)
    for sample in MClist:
        newfile = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/hSS_{}.root".format(year,sample),"read")
        newhist = newfile.Get(histname)
        h_tmp = hBKGOS - newhist
        hBKGOS = h_tmp
    fout.cd()
    hBKGOS.SetName("Fake")
    hBKGOS.Write()