from ROOT import RDataFrame, TFile, TChain, TTree, TH1D, TLorentzVector, TCanvas
import numpy
import sys
from math import cos, sin, sqrt, pi
import ROOT
import time as timer
ROOT.EnableImplicitMT()
year = sys.argv[1]
#name = sys.argv[2]
print("year is", year, "created fake bkg")

time_start = timer.time()
histnamelist = ["mvis","ptemu","nTrk","elept","mupt","eleeta","mueta", "Acopl", "MET", "deta", "mumtrans", "elemtrans"]
MClist = ["VV","Top","ZTT"]
fdataSS = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisSS/emu_{}_data.root".format(year),"read")
fout = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisSS/emu_{}_fake.root".format(year),"recreate")
for histname in histnamelist:
    hBKGOS = fdataSS.Get(histname)
    for sample in MClist:
        newfile = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisSS/emu_{}_{}.root".format(year,sample),"read")
        newhist = newfile.Get(histname)
        h_tmp = hBKGOS - newhist
        hBKGOS = h_tmp
    fout.cd()
    hBKGOS.Write()