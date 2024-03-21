from ROOT import RDataFrame, TFile, TChain, TTree, TH1D, TLorentzVector, TCanvas
import numpy
import sys
from math import cos, sin, sqrt, pi
import ROOT
import time as timer
time_start = timer.time()
ROOT.EnableImplicitMT()
year = sys.argv[1]
sample = sys.argv[2]

print("year is", year, "sample is", sample)

df = RDataFrame("Events","/eos/user/z/zohe/WWdata/inclusive/ntuples_emu_{}_basicsel/{}.root".format(year,sample))
if "MuonEG" in sample:
    df = df.Define("allweight","1.0")
else:
    df = df.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight")
    
df = df.Filter("isOS==0")
h_mvis = df.Histo1D(("mvis","mvis",485,15,500),"mvis","allweight")
h_ptemu = df.Histo1D(("ptemu","ptemu",270,30,300),"ptemu","allweight")
h_nTrk = df.Histo1D(("nTrk","nTrk",100,0,100),"nTrk","allweight")
h_elept = df.Histo1D(("elept","elept",100,20,120),"elept","allweight")
h_mupt = df.Histo1D(("mupt","mupt",100,20,120),"mupt","allweight")
h_eleeta = df.Histo1D(("eleeta","eleeta",52,-2.5,2.7),"eleeta","allweight")
h_mueta = df.Histo1D(("mueta","mueta",52,-2.5,2.7),"mueta","allweight")
fout = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisSS/emu_{}_{}.root".format(year,sample),"recreate")
h_mvis.Write()
h_ptemu.Write()
h_nTrk.Write()
h_elept.Write()
h_mupt.Write()
h_eleeta.Write()
h_mueta.Write()