from ROOT import RDataFrame, TFile, TChain, TTree, TH1D, TLorentzVector, TCanvas
import numpy
import sys
from math import cos, sin, sqrt, pi
import ROOT
import time as timer
ROOT.EnableImplicitMT()
year = sys.argv[1]
name = sys.argv[2]
print("year is", year, "created fake bkg")

time_start = timer.time()
histnamelist = ["ptemu"]
MClist = ["VV","Top","ZTT"]
if name == "nTrk0":
    fdataSS = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/h0SS_data.root".format(year),"read")
    fout = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/h0_Fake.root".format(year),"recreate")
elif name == "nTrk1":
    fdataSS = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/h1SS_data.root".format(year),"read")
    fout = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/h1_Fake.root".format(year),"recreate")
for histname in histnamelist:
    hBKGOS = fdataSS.Get(histname)
    for sample in MClist:
        if name == "nTrk0":
            newfile = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/h0SS_{}.root".format(year,sample),"read")
        elif name == "nTrk1":
            newfile = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/h1SS_{}.root".format(year,sample),"read")
        newhist = newfile.Get(histname)
        h_tmp = hBKGOS - newhist
        hBKGOS = h_tmp
    fout.cd()
    hBKGOS.SetName("Fake_puWeightDown")
    hBKGOS.Write()