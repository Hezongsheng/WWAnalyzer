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

print("year is", year, "sample is", sample, "name is", name, "SS")
if name=="inclusive":
    df = RDataFrame("Events","/eos/user/z/zohe/WWdata/inclusive/ntuples_emu_{}_basicsel/{}.root".format(year,sample))
elif "exclusive" in name:
    df = RDataFrame("Events","/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/{}.root".format(year,sample))
df = df.Define("deta","abs(eleeta-mueta)")
    
if sample=="data":
    df = df.Define("allweight","FRweight")
else:
    df = df.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight*Acoweight*topptweight*FRweight")

if name=="exclusive0":
    df = df.Filter("nTrk==0")
elif name=="exclusive1":
    df = df.Filter("nTrk==1")
elif name=="exclusive01":
    df = df.Filter("nTrk<=1")
df = df.Filter("!isOS")
'''
if "exclusive" in name:
    df = df.Filter("ptemu>70")
'''
h_mvis = df.Histo1D(("mvis","mvis",500,0,500),"mvis","allweight")
h_ptemu = df.Histo1D(("ptemu","ptemu",300,0,300),"ptemu","allweight")
h_nTrk = df.Histo1D(("nTrk","nTrk",100,0,100),"nTrk","allweight")
h_elept = df.Histo1D(("elept","elept",120,0,120),"elept","allweight")
h_mupt = df.Histo1D(("mupt","mupt",120,0,120),"mupt","allweight")
h_eleeta = df.Histo1D(("eleeta","eleeta",50,-2.5,2.5),"eleeta","allweight")
h_mueta = df.Histo1D(("mueta","mueta",50,-2.5,2.5),"mueta","allweight")
h_Acopl = df.Histo1D(("Acopl","Acopl",100,0.0,1.0),"Acopl","allweight")
h_MET = df.Histo1D(("MET","MET",120,0.0,120.0),"MET_pt","allweight")
h_deta = df.Histo1D(("deta","deta",100,0.0,5.0),"deta","allweight")
h_mumtrans = df.Histo1D(("mumtrans","mumtrans",180,0.0,180.0),"mumtrans","allweight")
h_elemtrans = df.Histo1D(("elemtrans","elemtrans",180,0.0,180.0),"elemtrans","allweight")
Hlist = [h_mvis, h_ptemu, h_nTrk, h_elept, h_mupt, h_eleeta, h_mueta, h_Acopl, h_deta]
for h in Hlist:
    overflow = h.GetBinContent(h.GetNbinsX())+h.GetBinContent(h.GetNbinsX()+1)
    h.SetBinContent(h.GetNbinsX(), overflow)
    #underflow = h.GetBinContent(0)+h.GetBinContent(1)
    #h.SetBinContent(1, underflow)
fout = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisSS/emu_{}_{}.root".format(year,sample),"recreate")
h_mvis.Write()
h_ptemu.Write()
h_nTrk.Write()
h_elept.Write()
h_mupt.Write()
h_eleeta.Write()
h_mueta.Write()
h_Acopl.Write()
h_MET.Write()
h_deta.Write()
h_mumtrans.Write()
h_elemtrans.Write()