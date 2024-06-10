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
print("year is", year, "sample is", sample)
df = RDataFrame("Events","/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/{}.root".format(year,sample))
df = df.Filter("!isOS").Filter("nTrk<=1")
df = df.Filter("ptemu>40")

if sample=="data":
    df = df.Define("allweight","FRweight")
else:
    df = df.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight*Acoweight*topptweight*FRweight")

h_pt = df.Histo1D(("ptemu","ptemu",14,40,180),"ptemu","allweight")
fout = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/hSS_{}.root".format(year,sample),"recreate")
h_pt.Write()