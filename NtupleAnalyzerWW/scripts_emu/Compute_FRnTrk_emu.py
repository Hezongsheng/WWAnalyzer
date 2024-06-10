from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector, TCanvas, TH2D
import numpy as numpy
import sys
from math import cos, sin, sqrt, pi
import ROOT
import time as timer
from array import array
ROOT.gInterpreter.AddIncludePath('/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/lib')
#ROOT.gInterpreter.Declare('#include "basic_sel.h"')
#ROOT.gInterpreter.Declare('#include "GetPFTrk.h"')
ROOT.gInterpreter.Declare('#include "Correction.h"')
#ROOT.gInterpreter.Declare('#include "myHelper.h"')
ROOT.gSystem.Load('/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/lib/RDFfunc.so')
ROOT.EnableImplicitMT();
year = sys.argv[1]
print("Computing FR nTrk correction for year", year)
#sample = sys.argv[2]
#print("year is", year, "sample is", sample)

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat("1.2f")


postfixName=[""]
#samplelist = ["data","VV","DY","top"]

def add_lumi(year):
    lowX=0.35
    lowY=0.835
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.30, lowY+0.16, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.055)
    lumi.SetTextFont (   42 )
    if (year=="2018"): lumi.AddText("2018, 60 fb^{-1} (13 TeV)")
    if (year=="2017"): lumi.AddText("2017, 41 fb^{-1} (13 TeV)")
    if (year=="2016"): lumi.AddText("2016, 36 fb^{-1} (13 TeV)")
    if (year=="2016pre"): lumi.AddText("2016 preVFP, 20 fb^{-1} (13 TeV)")
    if (year=="2016post"): lumi.AddText("2016 postVFP, 16 fb^{-1} (13 TeV)")
    return lumi

def add_CMS():
    lowX=0.16
    lowY=0.835
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(61)
    lumi.SetTextSize(0.065)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("CMS")
    return lumi


df_MC = RDataFrame("Events","/eos/user/z/zohe/WWdata/FR/ntuples_emu_{}_basicsel/MC.root".format(year))
df_MC = df_MC.Filter("!isOS").Filter("eleiso").Filter("muiso")
df_MC = df_MC.Define("OStoSS","Get_OStoSS(elept,mupt,\"{}\")".format(year)).Define("antimuCor","Get_antimuCor(elept,mupt,\"{}\")".format(year))
df_MC = df_MC.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight").Define("allweight_OStoSS","allweight*OStoSS").Define("allweight_antimuCor","allweight*antimuCor")

#print("OK1")

sum_weight = df_MC.Sum("allweight").GetValue()
sum_weight_OStoSS = df_MC.Sum("allweight_OStoSS").GetValue()/sum_weight
sum_weight_antimuCor = df_MC.Sum("allweight_antimuCor").GetValue()/sum_weight
h_OStoSS = ROOT.TH1D("OStoSSCor","OStoSSCor",101,0,101)
h_antimuCor = ROOT.TH1D("antimuCorCor","antimuCorCor",101,0,101)

#print("OK2")

for i in range(101):
    df_using = df_MC.Filter("nTrk=={}".format(i))
    sum_weight_using = df_using.Sum("allweight").GetValue()
    sum_weight_OStoSS_using = df_using.Sum("allweight_OStoSS").GetValue()
    sum_weight_antimuCor_using = df_using.Sum("allweight_antimuCor").GetValue()
    OStoSSCor = (sum_weight_OStoSS_using/sum_weight_using)/sum_weight_OStoSS
    antimuCorCor = (sum_weight_antimuCor_using/sum_weight_using)/sum_weight_antimuCor
    h_OStoSS.SetBinContent(i,OStoSSCor)
    h_antimuCor.SetBinContent(i,antimuCorCor)

fout = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/FRnTrk_{}.root".format(year),"recreate")
#print("OK3")
c=ROOT.TCanvas("canvas","",0,0,800,800)
c.SetRightMargin(0.15)

c.cd()
h_OStoSS.SetTitle("")
h_OStoSS.SetName("OS-to-SS_nTrkCor")
h_OStoSS.SetMarkerStyle(20)
h_OStoSS.SetMarkerColor(1)
h_OStoSS.SetLineColor(1)
h_OStoSS.GetXaxis().SetTitle("N_{tracks}")
h_OStoSS.GetYaxis().SetTitle("OS-to-SS ratio/avarege")
h_OStoSS.Draw()
lumi=add_lumi(year)
lumi.Draw("same")
cms=add_CMS()
cms.Draw("same")
fout.cd()
h_OStoSS.Write()

c.cd()
c.Modified()
c.SaveAs("OS-to-SS_nTrkCor_"+year+".pdf")
c.SaveAs("OS-to-SS_nTrkCor_"+year+".png")

c.cd()
h_antimuCor.SetTitle("")
h_antimuCor.SetName("anti-mu_nTrkCor")
h_antimuCor.SetMarkerStyle(20)
h_antimuCor.SetMarkerColor(1)
h_antimuCor.SetLineColor(1)
h_antimuCor.GetXaxis().SetTitle("N_{tracks}")
h_antimuCor.GetYaxis().SetTitle("anti-\mu correction/avarege")
h_antimuCor.Draw()
lumi=add_lumi(year)
lumi.Draw("same")
cms=add_CMS()
cms.Draw("same")
fout.cd()
h_antimuCor.Write()

c.cd()
c.Modified()
c.SaveAs("antimuCor_nTrkCor_"+year+".pdf")
c.SaveAs("antimuCor_nTrkCor_"+year+".png")
