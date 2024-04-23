#!/usr/bin/env python
import sys
#sys.path.append("..")
import ROOT
import re
import argparse
from array import array
import numpy as np
#from pyFunc.gethisto_SR_mutau import variable

class variable:
    def __init__(self, name, title, nbins, binning):
        self.name=name
        self.title = title
        self.nbins=nbins
        self.binning = binning


def add_lumi(year):
    lowX=0.55
    lowY=0.835
    if (year=="2016pre" or year=="2016post"): lowX = 0.45
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.30, lowY+0.16, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.06)
    lumi.SetTextFont (   42 )
    if (year=="2018"): lumi.AddText("2018, 60 fb^{-1} (13 TeV)")
    if (year=="2016pre"): lumi.AddText("2016 preVFP, 19 fb^{-1} (13 TeV)")
    if (year=="2016post"): lumi.AddText("2016 postVFP, 16 fb^{-1} (13 TeV)")
    if (year=="2017"): lumi.AddText("2017, 41 fb^{-1} (13 TeV)")
    if (year=="2016"): lumi.AddText("2016, 36 fb^{-1} (13 TeV)")
    return lumi

def add_CMS():
    lowX=0.21
    lowY=0.70
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(61)
    lumi.SetTextSize(0.08)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("CMS")
    return lumi

def add_Preliminary():
    lowX=0.21
    lowY=0.63
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(52)
    lumi.SetTextSize(0.06)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("Preliminary")
    return lumi

def make_legend():
    output = ROOT.TLegend(0.5, 0.65, 0.92, 0.86, "", "brNDC")
    output.SetNColumns(2)
    output.SetLineWidth(0)
    output.SetLineStyle(0)
    output.SetFillStyle(0)
    output.SetBorderSize(0)
    output.SetTextFont(62)
    return output

def make_legend2():
    output = ROOT.TLegend(0.45, 0.6, 0.92, 0.86, "", "brNDC")
    output.SetNColumns(2)
    output.SetLineWidth(0)
    output.SetLineStyle(0)
    output.SetFillStyle(0)
    output.SetBorderSize(0)
    output.SetTextFont(62)
    return output
    
    
ROOT.gStyle.SetOptStat(0)

parser = argparse.ArgumentParser()
parser.add_argument('--year', '-y', default=None, help='Year to draw')
#parser.add_argument('--channel', '-c', default=None, help='channel to draw')
parser.add_argument('--variable', '-v', default=None, help='Variable to draw')
args = parser.parse_args()


mvis = variable("mvis","m_{vis}",int(21),np.array([15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,300,500],dtype=float))
elept = variable("elept","e p_{T}",int(39),np.array([20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
mupt = variable("mupt","#mu p_{T}",int(39),np.array([20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
Aco = variable("Acopl","acoplanarity",int(40),np.arange(0,1.025,0.025,dtype=float))
mtranse = variable("mtrans","m_{T}(#mu,MET)",int(36),np.arange(0,185,5,dtype=float))
nTrk = variable("nTrk","N_{tracks}",int(50),np.arange(0,102,2,dtype=float))
MET = variable("MET_pt","MET",int(19),np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,80,90,100,110,120],dtype=float))
eleeta = variable("eleeta","e #eta", int(50), np.arange(-2.5,2.6,0.1,dtype=float))
mueta = variable("mueta","#mu #eta", int(50), np.arange(-2.5,2.6,0.1,dtype=float))
ptemu = variable("ptemu","pt_{e#mu}",int(33),np.arange(15,185,5,dtype=float))

variablelist = [mvis,elept,mupt,Aco,mtranse,nTrk,MET,eleeta,mueta,ptemu]

title="m_{vis}"
for var in variablelist:
    if args.variable == var.name:
        title = var.title
        var_used = var
        
c=ROOT.TCanvas("canvas","",0,0,800,800)
c.cd()

'''
file=ROOT.TFile("Histo/HistoInclu_{}/Inclusive_all.root".format(args.year),"r")
'''

adapt=ROOT.gROOT.GetColor(12)
new_idx=ROOT.gROOT.GetListOfColors().GetSize() + 1
trans=ROOT.TColor(new_idx, adapt.GetRed(), adapt.GetGreen(),adapt.GetBlue(), "",0.5)
#title="#tau p_{T}"
#title="#mu p_{T}"



'''
Data=file.Get(args.channel).Get("data_obs")
#W=file.Get(categories[i]).Get("W")
TT=file.Get(args.channel).Get("TT")
VV=file.Get(args.channel).Get("VV")
ZTT=file.Get(args.channel).Get("ZTT")
ZLL = file.Get(args.channel).Get("ZLL")
ST=file.Get(args.channel).Get("ST")
#GGTT=file.Get(args.channel).Get("GGTT")
VV.Add(ST.Clone())
#VV.Add(W.Clone())
Fake=file.Get(args.channel).Get("Fake")
'''
fData = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_MuonEG.root".format(args.year),"r")
hData = ROOT.TH1D(fData.Get(args.variable)) 
Data = ROOT.TH1D("Data","new hist of Data",var_used.nbins,var_used.binning)
for i in range(1, hData.GetNbinsX() + 1):
    new_bin_index = Data.FindBin(hData.GetBinCenter(i))
    #print(new_bin_index)
    Data.SetBinContent(new_bin_index, Data.GetBinContent(new_bin_index) + hData.GetBinContent(i))





fVV = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_VV.root".format(args.year),"r")
hVV = ROOT.TH1D(fVV.Get(args.variable)) 
VV = ROOT.TH1D("VV","new hist of VV",var_used.nbins,var_used.binning)
for i in range(1, hVV.GetNbinsX() + 1):
    new_bin_index = VV.FindBin(hVV.GetBinCenter(i))
    VV.SetBinContent(new_bin_index, VV.GetBinContent(new_bin_index) + hVV.GetBinContent(i))

fFake = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisSS/emu_{}_fake.root".format(args.year),"r")
hFake = ROOT.TH1D(fFake.Get(args.variable)) 
Fake = ROOT.TH1D("Fake","new hist of Fake",var_used.nbins,var_used.binning)
for i in range(1, hData.GetNbinsX() + 1):
    new_bin_index = Fake.FindBin(hFake.GetBinCenter(i))
    Fake.SetBinContent(new_bin_index, Fake.GetBinContent(new_bin_index) + hFake.GetBinContent(i))

fDYemu = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_DYemu.root".format(args.year),"r")
hDYemu = ROOT.TH1D(fDYemu.Get(args.variable))
DYemu = ROOT.TH1D("DYemu","new hist of DYemu",var_used.nbins,var_used.binning)
for i in range(1, hDYemu.GetNbinsX() + 1):
    new_bin_index = DYemu.FindBin(hDYemu.GetBinCenter(i))
    DYemu.SetBinContent(new_bin_index, DYemu.GetBinContent(new_bin_index) + hDYemu.GetBinContent(i))

ftop = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_top.root".format(args.year),"r")
htop = ROOT.TH1D(ftop.Get(args.variable)) 
top = ROOT.TH1D("top","new hist of top",var_used.nbins,var_used.binning)
for i in range(1, htop.GetNbinsX() + 1):
    new_bin_index = top.FindBin(hData.GetBinCenter(i))
    top.SetBinContent(new_bin_index, top.GetBinContent(new_bin_index) + htop.GetBinContent(i))

Data.GetXaxis().SetTitle("")
Data.GetXaxis().SetTitleSize(0)
Data.GetXaxis().SetNdivisions(505)

Data.GetYaxis().SetLabelFont(42)
Data.GetYaxis().SetLabelOffset(0.01)
Data.GetYaxis().SetLabelSize(0.06)
Data.GetYaxis().SetTitleSize(0.075)
Data.GetYaxis().SetTitleOffset(1.04)
Data.SetTitle("")
Data.GetYaxis().SetTitle("Events/bin")
Data.SetMinimum(0.1)



#blind
if args.variable=="nTrk":
    for k in range(1,2):
        Data.SetBinContent(k,0.0)
print(type(top))

VV.SetFillColor(ROOT.TColor.GetColor("#f6cd61"))
Fake.SetFillColor(ROOT.TColor.GetColor("#3da4ab"))
DYemu.SetFillColor(ROOT.TColor.GetColor("#969df1"))
top.SetFillColor(ROOT.TColor.GetColor("#4a4e4d"))

Data.SetMarkerStyle(20)
Data.SetMarkerSize(1)
#ZTT.SetLineColor(1)
VV.SetLineColor(1)
Fake.SetLineColor(1)
DYemu.SetLineColor(1)
top.SetLineColor(1)
Data.SetLineColor(1)
Data.SetLineWidth(2)

#GGTT.SetLineColor(2)
#GGTT.SetLineWidth(3)

stack=ROOT.THStack("stack","stack")
stack.Add(VV)
stack.Add(Fake)
stack.Add(DYemu)
stack.Add(top)

errorBand = VV.Clone()
errorBand.Add(Fake)
errorBand.Add(DYemu)
errorBand.Add(top)

errorBand.SetMarkerSize(0)
errorBand.SetFillColor(new_idx)
errorBand.SetFillStyle(3001)
errorBand.SetLineWidth(1)

pad1 = ROOT.TPad("pad1","pad1",0,0.35,1,1)
pad1.Draw()
pad1.cd()
pad1.SetFillColor(0)
pad1.SetBorderMode(0)
pad1.SetBorderSize(10)
pad1.SetTickx(1)
pad1.SetTicky(1)
pad1.SetLeftMargin(0.18)
pad1.SetRightMargin(0.05)
pad1.SetTopMargin(0.122)
pad1.SetBottomMargin(0.026)
pad1.SetFrameFillStyle(0)
pad1.SetFrameLineStyle(0)
pad1.SetFrameBorderMode(0)
pad1.SetFrameBorderSize(10)
#pad1.SetLogy()

Data.GetXaxis().SetLabelSize(0)
Data.SetMaximum(max(Data.GetMaximum()*1.5,errorBand.GetMaximum()*1.5))
Data.SetMinimum(0.1)
Data.Draw("e")
stack.Draw("histsame")
errorBand.Draw("e2same")
Data.Draw("esame")

#GGTT.Draw("histsame")

legende=make_legend()
legende.AddEntry(Data,"Observed","elp")

legende.AddEntry(VV,"VV","f")
legende.AddEntry(Fake,"Fake","f")
legende.AddEntry(DYemu,"Drell Yan","f")
legende.AddEntry(top,"top","f")
#legende.AddEntry(GGTT,"Signal x 10","l")
legende.AddEntry(errorBand,"Uncertainty","f")
legende.Draw()

l1=add_lumi(args.year)
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")

pad1.RedrawAxis()

c.cd()
pad2 = ROOT.TPad("pad2","pad2",0,0,1,0.35);
pad2.SetTopMargin(0.05);
pad2.SetBottomMargin(0.35);
pad2.SetLeftMargin(0.18);
pad2.SetRightMargin(0.05);
pad2.SetTickx(1)
pad2.SetTicky(1)
pad2.SetGridx()
pad2.SetGridy()
pad2.Draw()
pad2.cd()
h1=Data.Clone()
h1.SetMaximum(1.3)#FIXME(3)
h1.SetMinimum(0.7)#FIXME(0.5)
h1.SetMarkerStyle(20)
h3=errorBand.Clone()
hwoE=errorBand.Clone()

for iii in range (1,hwoE.GetSize()-1):
    hwoE.SetBinError(iii,0)
h3.Sumw2()
h1.Sumw2()
h1.SetStats(0)
h1.Divide(hwoE)
h3.Divide(hwoE)
h1.GetXaxis().SetTitle(title)
h1.GetXaxis().SetLabelSize(0.08)
h1.GetYaxis().SetLabelSize(0.08)
h1.GetYaxis().SetTitle("Obs./Exp.")
h1.GetXaxis().SetNdivisions(505)
h1.GetYaxis().SetNdivisions(5)

h1.GetXaxis().SetTitleSize(0.15)
h1.GetYaxis().SetTitleSize(0.15)
h1.GetYaxis().SetTitleOffset(0.56)
h1.GetXaxis().SetTitleOffset(1.04)
h1.GetXaxis().SetLabelSize(0.11)
h1.GetYaxis().SetLabelSize(0.11)
h1.GetXaxis().SetTitleFont(42)
h1.GetYaxis().SetTitleFont(42)

h1.Draw("e0p")
h3.Draw("e2same")

c.cd()
pad1.Draw()

ROOT.gPad.RedrawAxis()

c.Modified()
c.SaveAs("Plotsemu/"+args.year+"inclusive/control_"+args.variable+".pdf")
c.SaveAs("Plotsemu/"+args.year+"inclusive/control_"+args.variable+".png")