from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector, TCanvas
import numpy as numpy
import sys
from math import cos, sin, sqrt, pi
import ROOT
import time as timer
time_start = timer.time()
ROOT.gInterpreter.AddIncludePath('/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/lib')
ROOT.gInterpreter.Declare('#include "basic_sel.h"')
ROOT.gInterpreter.Declare('#include "GetPFTrk.h"')
ROOT.gInterpreter.Declare('#include "Correction.h"')
ROOT.gInterpreter.Declare('#include "myHelper.h"')
ROOT.gSystem.Load('/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/lib/RDFfunc.so')
ROOT.EnableImplicitMT();

year = sys.argv[1]
sample = sys.argv[2]
name = sys.argv[3]
print("year is", year, "sample is", sample)
df = RDataFrame("Events","/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/{}.root".format(year,sample))
df = df.Filter("!isOS")
if name=="nTrk0":
    df = df.Filter("nTrk==0")
    fout = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/h0SS_{}.root".format(year,sample),"recreate")
elif name=="nTrk1":
    df = df.Filter("nTrk==1")
    fout = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/h1SS_{}.root".format(year,sample),"recreate")
#df = df.Filter("ptemu>30")

if sample=="data":
    df = df.Define("allweight","FRweight")
else:
    df = df.Define("allweight","xsweight*puWeightDown*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight*Acoweight*topptweight*FRweight")

h_ptemu = df.Histo1D(("ptemu","ptemu",18,0,180),"ptemu","allweight")
Hlist = [h_ptemu]
for h in Hlist:
    overflow = h.GetBinContent(h.GetNbinsX())+h.GetBinContent(h.GetNbinsX()+1)
    h.SetBinContent(h.GetNbinsX(), overflow)
fout.cd()
h_ptemu.Write()