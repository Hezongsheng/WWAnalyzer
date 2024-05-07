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
name = sys.argv[3]

print("year is", year, "sample is", sample, "name is", name, "OS")
if name == "inclusive":
    df = RDataFrame("Events","/eos/user/z/zohe/WWdata/inclusive/ntuples_emu_{}_basicsel/{}.root".format(year,sample))
elif "exclusive" in name:
    df = RDataFrame("Events","/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/{}.root".format(year,sample))

if "MuonEG" in sample:
    df = df.Define("allweight","1.0")
else:
    if "GGToWW" in sample and name == "inclusive":
        df = df.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight*1e3")
    elif "GGToWW" in sample and "exclusive" in name:
        df = df.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight*1")
    elif "GGToTauTau" in sample and "exclusive" in name:
        df = df.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight*TauG2Weights_ceBRe_0p0*1")    
    else:
        df = df.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight")


if name=="exclusive0":
    df = df.Filter("isOS==1").Filter("nTrk==0")
elif name=="exclusive1":
    df = df.Filter("isOS==1").Filter("nTrk==1")
h_mvis = df.Histo1D(("mvis","mvis",485,15,500),"mvis","allweight")
h_ptemu = df.Histo1D(("ptemu","ptemu",285,15,300),"ptemu","allweight")
h_nTrk = df.Histo1D(("nTrk","nTrk",100,0,100),"nTrk","allweight")
h_elept = df.Histo1D(("elept","elept",100,20,120),"elept","allweight")
h_mupt = df.Histo1D(("mupt","mupt",100,20,120),"mupt","allweight")
h_eleeta = df.Histo1D(("eleeta","eleeta",52,-2.5,2.7),"eleeta","allweight")
h_mueta = df.Histo1D(("mueta","mueta",52,-2.5,2.7),"mueta","allweight")
h_Acopl = df.Histo1D(("Acopl","Acopl",100,0.0,1.0),"Acopl","allweight")
Hlist = [h_mvis, h_ptemu, h_nTrk, h_elept, h_mupt, h_eleeta, h_mueta, h_Acopl]
for h in Hlist:
    overflow = h.GetBinContent(h.GetNbinsX())+h.GetBinContent(h.GetNbinsX()+1)
    h.SetBinContent(h.GetNbinsX(), overflow)
    #underflow = h.GetBinContent(0)+h.GetBinContent(1)
    #h.SetBinContent(1, underflow)

fout = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_{}.root".format(year,sample),"recreate")
h_mvis.Write()
h_ptemu.Write()
h_nTrk.Write()
h_elept.Write()
h_mupt.Write()
h_eleeta.Write()
h_mueta.Write()
h_Acopl.Write()