#!/usr/bin/env python
import sys
#sys.path.append("..")
import ROOT
import re
import argparse
from array import array
import numpy as np
#from pyFunc.gethisto_SR_mutau import variable
year = sys.argv[1]
variables = sys.argv[2]
name = sys.argv[3]


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

def add_nTrk(name):
    lowX=0.2
    lowY=0.835
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.30, lowY+0.16, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.1)
    lumi.SetTextFont (   42 )
    if (name=="exclusive0"): lumi.AddText("nTrk=0")
    elif (name=="exclusive1"): lumi.AddText("nTrk=1")
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

#parser = argparse.ArgumentParser()
#parser.add_argument('--year', '-y', default=None, help='Year to draw')
#parser.add_argument('--channel', '-c', default=None, help='channel to draw')
#parser.add_argument('--variable', '-v', default=None, help='Variable to draw')
#parser.add_argument('--name', '-n', default=None, help='Name of the plot')
#args = parser.parse_args()



mvis = variable("mvis","m_{vis}",int(22),np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,300,500],dtype=float))
elept = variable("elept","e p_{T}",int(44),np.array([10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
mupt = variable("mupt","#mu p_{T}",int(44),np.array([10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
Aco = variable("Acopl","acoplanarity",int(50),np.arange(0,1.02,0.02,dtype=float))
mtranse = variable("mtrans","m_{T}(#mu,MET)",int(36),np.arange(0,185,5,dtype=float))
nTrk = variable("nTrk","N_{tracks}",int(50),np.arange(0,102,2,dtype=float))
MET = variable("MET_pt","MET",int(19),np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,80,90,100,110,120],dtype=float))
eleeta = variable("eleeta","e #eta", int(50), np.arange(-2.5,2.6,0.1,dtype=float))
mueta = variable("mueta","#mu #eta", int(50), np.arange(-2.5,2.6,0.1,dtype=float))
ptemu = variable("ptemu","pt_{e#mu}",int(36),np.arange(0,185,5,dtype=float))

variablelist = [mvis,elept,mupt,Aco,mtranse,nTrk,MET,eleeta,mueta,ptemu]

title="m_{vis}"
for var in variablelist:
    if variables == var.name:
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
fData = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_data.root".format(year),"r")
hData = ROOT.TH1D(fData.Get(variables)) 
Data = ROOT.TH1D("Data","new hist of Data",var_used.nbins,var_used.binning)
for i in range(1, hData.GetNbinsX() + 1):
    new_bin_index = Data.FindBin(hData.GetBinCenter(i))
    #print(new_bin_index)
    Data.SetBinContent(new_bin_index, Data.GetBinContent(new_bin_index) + hData.GetBinContent(i))





fVV = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_VV.root".format(year),"r")
hVV = ROOT.TH1D(fVV.Get(variables)) 
VV = ROOT.TH1D("VV","new hist of VV",var_used.nbins,var_used.binning)
for i in range(1, hVV.GetNbinsX() + 1):
    new_bin_index = VV.FindBin(hVV.GetBinCenter(i))
    VV.SetBinContent(new_bin_index, VV.GetBinContent(new_bin_index) + hVV.GetBinContent(i))

fFake = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisSS/emu_{}_fake.root".format(year),"r")
hFake = ROOT.TH1D(fFake.Get(variables)) 
Fake = ROOT.TH1D("Fake","new hist of Fake",var_used.nbins,var_used.binning)
for i in range(1, hData.GetNbinsX() + 1):
    new_bin_index = Fake.FindBin(hFake.GetBinCenter(i))
    Fake.SetBinContent(new_bin_index, Fake.GetBinContent(new_bin_index) + hFake.GetBinContent(i))

fDY = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_DY.root".format(year),"r")
hDY = ROOT.TH1D(fDY.Get(variables))
DY = ROOT.TH1D("DY","new hist of DY",var_used.nbins,var_used.binning)
for i in range(1, hDY.GetNbinsX() + 1):
    new_bin_index = DY.FindBin(hDY.GetBinCenter(i))
    DY.SetBinContent(new_bin_index, DY.GetBinContent(new_bin_index) + hDY.GetBinContent(i))

ftop = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_top.root".format(year),"r")
htop = ROOT.TH1D(ftop.Get(variables)) 
top = ROOT.TH1D("top","new hist of top",var_used.nbins,var_used.binning)
for i in range(1, htop.GetNbinsX() + 1):
    new_bin_index = top.FindBin(hData.GetBinCenter(i))
    top.SetBinContent(new_bin_index, top.GetBinContent(new_bin_index) + htop.GetBinContent(i))

if "exclusive" in name:
    fGG2WW = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_GGToWW.root".format(year),"r")
    hGG2WW = ROOT.TH1D(fGG2WW.Get(variables)) 
    GG2WW = ROOT.TH1D("GG2WW","new hist of GG2WW",var_used.nbins,var_used.binning)
    for i in range(1, hGG2WW.GetNbinsX() + 1):
        new_bin_index = GG2WW.FindBin(hData.GetBinCenter(i))
        GG2WW.SetBinContent(new_bin_index, GG2WW.GetBinContent(new_bin_index) + hGG2WW.GetBinContent(i))


    fGG2TauTau = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_GGToTauTau.root".format(year),"r")
    hGG2TauTau = ROOT.TH1D(fGG2TauTau.Get(variables)) 
    GG2TauTau = ROOT.TH1D("GG2TauTau","new hist of GG2TauTau",var_used.nbins,var_used.binning)
    for i in range(1, hGG2TauTau.GetNbinsX() + 1):
        new_bin_index = GG2TauTau.FindBin(hData.GetBinCenter(i))
        GG2TauTau.SetBinContent(new_bin_index, GG2TauTau.GetBinContent(new_bin_index) + hGG2TauTau.GetBinContent(i))
    nGG2WW = 0
    for i in range(1,GG2WW.GetSize()+1):
        nGG2WW += GG2WW.GetBinContent(i)
    print("nGG2WW", nGG2WW/10)
    nGG2TauTau = 0
    for i in range(1,GG2TauTau.GetSize()+1):
        nGG2TauTau += GG2TauTau.GetBinContent(i)
    print("nGG2TauTau", nGG2TauTau/10)
    nVV = 0
    for i in range(1,VV.GetSize()+1):
            nVV += VV.GetBinContent(i)
    print("nVV", nVV)
    nFake = 0
    for i in range(1,Fake.GetSize()+1):
        nFake += Fake.GetBinContent(i)
    print("nFake", nFake)
    nDY = 0
    for i in range(1,DY.GetSize()+1):
        nDY += DY.GetBinContent(i)
    print("nDY", nDY)
    ntop = 0
    for i in range(1,top.GetSize()+1):
        ntop += top.GetBinContent(i)
    print("ntop", ntop) 
    nBKG = nVV + nFake + nDY + ntop + nGG2TauTau/10
    print("nBKG", nBKG)
if name=="inclusive":
    Data.GetXaxis().SetTitle("")
    Data.GetXaxis().SetTitleSize(0)
    Data.GetXaxis().SetNdivisions(505)
elif "exclusive" in name:
    Data.GetXaxis().SetTitle(title)
    Data.GetXaxis().SetNdivisions(505)
    Data.GetXaxis().SetTitleSize(0.075)
    Data.GetXaxis().SetTitleOffset(0.6)
    Data.GetXaxis().SetLabelSize(0.06)
    Data.GetXaxis().SetTitleFont(42)

Data.GetYaxis().SetLabelFont(42)
Data.GetYaxis().SetLabelOffset(0.01)
Data.GetYaxis().SetLabelSize(0.06)
Data.GetYaxis().SetTitleSize(0.075)
Data.GetYaxis().SetTitleOffset(1.04)
Data.SetTitle("")

if variables=="mvis":
    Data.GetYaxis().SetTitle("Events/10GeV")
elif variables=="elept" or variables=="mupt":
    Data.GetYaxis().SetTitle("Events/2GeV")
elif variables=="Aco":
    Data.GetYaxis().SetTitle("Events/0.025")
elif variables=="mtrans":
    Data.GetYaxis().SetTitle("Events/5GeV")
elif variables=="MET":
    Data.GetYaxis().SetTitle("Events/5GeV")
elif variables=="eleeta" or variables=="mueta":
    Data.GetYaxis().SetTitle("Events/0.1")
elif variables=="ptemu":
    Data.GetYaxis().SetTitle("Events/5GeV")
Data.SetMinimum(0.1)

#blind
if "exclusive" in name:
    for k in range(1,Data.GetSize()+1):
        Data.SetBinContent(k,0.0)


Data.SetMarkerStyle(20)
Data.SetMarkerSize(1)


VV.SetFillColor(ROOT.TColor.GetColor("#f6cd61"))
Fake.SetFillColor(ROOT.TColor.GetColor("#3da4ab"))
DY.SetFillColor(ROOT.TColor.GetColor("#969df1"))
top.SetFillColor(ROOT.TColor.GetColor("#4a4e4d"))
if "exclusive" in name:
    GG2WW.SetFillColor(ROOT.TColor.GetColor("#ff0000"))
    GG2TauTau.SetFillColor(ROOT.TColor.GetColor("#00ff00"))


#ZTT.SetLineColor(1)
VV.SetLineColor(1)
Fake.SetLineColor(1)
DY.SetLineColor(1)
top.SetLineColor(1)
Data.SetLineColor(1)
Data.SetLineWidth(2)

#GGTT.SetLineColor(2)
#GGTT.SetLineWidth(3)

stack=ROOT.THStack("stack","stack")
if "exclusive" in name:
    stack.Add(GG2WW)
    stack.Add(GG2TauTau)
stack.Add(VV)
stack.Add(Fake)
stack.Add(DY)
stack.Add(top)

    




errorBand = VV.Clone()
if "exclusive" in name:
    errorBand.Add(GG2WW)
    errorBand.Add(GG2TauTau)
errorBand.Add(Fake)
errorBand.Add(DY)
errorBand.Add(top)

errorBand.SetMarkerSize(0)
errorBand.SetFillColor(new_idx)
errorBand.SetFillStyle(3001)
errorBand.SetLineWidth(1)

pad1 = ROOT.TPad("pad1","pad1",0,0.35,1,1)
#if "exclusive" in name:
#    pad1.SetPad(0,0,1,1)
pad1.Draw()
pad1.cd()
pad1.SetFillColor(0)
pad1.SetBorderMode(0)
pad1.SetBorderSize(10)
pad1.SetTickx(1)
pad1.SetTicky(1)
pad1.SetLeftMargin(0.18)
pad1.SetRightMargin(0.05)
if name=="inclusive":
    pad1.SetTopMargin(0.122)
    pad1.SetBottomMargin(0.026)
pad1.SetFrameFillStyle(0)
pad1.SetFrameLineStyle(0)
pad1.SetFrameBorderMode(0)
pad1.SetFrameBorderSize(10)
#pad1.SetLogy()


if name=="inclusive":
    Data.GetXaxis().SetLabelSize(0)
Data.SetMaximum(max(Data.GetMaximum()*1.5,errorBand.GetMaximum()*1.5))
Data.SetMinimum(0.1)
Data.Draw("e")
stack.Draw("histsame")
errorBand.Draw("e2same")
Data.Draw("esame")

    
    



#GGTT.Draw("histsame")

legende=make_legend()
if name=="inclusive":
    legende.AddEntry(Data,"Observed","elp")
    #legende.AddEntry(GG2WW,"Signal(GG#rightarrow WW)x1e3","f")
elif "exclusive" in name:
    legende.AddEntry(GG2WW,"Signal(GG#rightarrow WW)x10","f")
    legende.AddEntry(GG2TauTau,"GG#rightarrow #tau#taux10","f")
legende.AddEntry(VV,"VV","f")
legende.AddEntry(Fake,"Fake","f")
legende.AddEntry(DY,"Drell Yan","f")
legende.AddEntry(top,"top","f")
legende.AddEntry(errorBand,"Uncertainty","f")
legende.Draw()

l1=add_lumi(year)
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")
if "exclusive" in name:
    l4=add_nTrk(name)
    l4.Draw("same")
pad1.RedrawAxis()
if name=="inclusive":
    
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
if name=="inclusive":
    c.SaveAs("Plotsemu/"+year+"inclusive/control_"+variables+".pdf")
    c.SaveAs("Plotsemu/"+year+"inclusive/control_"+variables+".png")
elif name=="exclusive0":
    c.SaveAs("Plotsemu/"+year+"exclusive0/signal_"+variables+".pdf")
    c.SaveAs("Plotsemu/"+year+"exclusive0/signal_"+variables+".png")
elif name=="exclusive1":
    c.SaveAs("Plotsemu/"+year+"exclusive1/signal_"+variables+".pdf")
    c.SaveAs("Plotsemu/"+year+"exclusive1/signal_"+variables+".png")