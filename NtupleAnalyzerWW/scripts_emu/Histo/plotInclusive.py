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
    if (year=="run2"):lowX = 0.5
    if "inclusive" in name:
        lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.30, lowY+0.16, "NDC")
    elif "exclusive" in name:
        lumi  = ROOT.TPaveText(lowX, lowY+0.02, lowX+0.30, lowY+0.12, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    if "inclusive" in name:
        lumi.SetTextSize(0.06)
    elif "exclusive" in name:
        lumi.SetTextSize(0.04)
    lumi.SetTextFont (   42 )
    if (year=="2018"): lumi.AddText("2018, 60 fb^{-1} (13 TeV)")
    if (year=="2016pre"): lumi.AddText("2016 preVFP, 19 fb^{-1} (13 TeV)")
    if (year=="2016post"): lumi.AddText("2016 postVFP, 16 fb^{-1} (13 TeV)")
    if (year=="2017"): lumi.AddText("2017, 41 fb^{-1} (13 TeV)")
    if (year=="2016"): lumi.AddText("2016, 36 fb^{-1} (13 TeV)")
    if (year=="run2"): lumi.AddText("2016-2018, 137 fb^{-1} (13 TeV)")
    return lumi

def add_nTrk(name):
    lowX=0.2
    lowY=0.835
    lumi  = ROOT.TPaveText(lowX, lowY+0.02, lowX+0.30, lowY+0.12, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.04)
    lumi.SetTextFont (   42 )
    if (name=="exclusive0"): lumi.AddText("nTrk=0")
    elif (name=="exclusive1"): lumi.AddText("nTrk=1")
    elif (name=="exclusive01"): lumi.AddText("nTrk<=1")
    return lumi



def add_CMS():
    lowX=0.21
    lowY=0.70
    if "inclusive" in name:
        lumi = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    elif "exclusive" in name:
        lumi = ROOT.TPaveText(lowX, lowY+0.1, lowX+0.15, lowY+0.17, "NDC")
    lumi.SetTextFont(61)
    if "inclusive" in name:
        lumi.SetTextSize(0.08)
    elif "exclusive" in name:
        lumi.SetTextSize(0.05)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("CMS")
    return lumi

def add_Preliminary():
    lowX=0.21
    lowY=0.63
    if "inclusive" in name:
        lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
        lumi.SetTextSize(0.06)
    elif "exclusive" in name:
        lumi  = ROOT.TPaveText(lowX, lowY+0.12, lowX+0.15, lowY+0.19, "NDC")
        lumi.SetTextSize(0.04)
    lumi.SetTextFont(52)
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



mvis = variable("mvis","m_{vis}(GeV)",int(22),np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,300,500],dtype=float))
elept = variable("elept","e p_{T}(GeV)",int(44),np.array([10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
mupt = variable("mupt","#mu p_{T}(GeV)",int(44),np.array([10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
Acopl = variable("Acopl","acoplanarity",int(10),np.arange(0,1.1,0.1,dtype=float))
mumtrans = variable("mumtrans","m_{T}(#mu,MET)(GeV)",int(36),np.arange(0,185,5,dtype=float))
elemtrans = variable("elemtrans","m_{T}(e,MET)(GeV)",int(36),np.arange(0,185,5,dtype=float))
nTrk = variable("nTrk","N_{tracks}",int(50),np.arange(0,102,2,dtype=float))
MET = variable("MET","MET(GeV)",int(19),np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,80,90,100,110,120],dtype=float))
eleeta = variable("eleeta","e #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
mueta = variable("mueta","#mu #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
#ptemu = variable("ptemu","pt_{e#mu}",int(36),np.arange(0,185,5,dtype=float))
ptemu = variable("ptemu","p_{Te#mu}(GeV)",int(36),np.arange(0,185,5,dtype=float))
deta =  variable("deta","#Delta#eta(e,#mu)",int(50),np.arange(0,5.1,0.1,dtype=float))


variablelist = [mvis,elept,mupt,Acopl,nTrk,MET,eleeta,mueta,ptemu,deta, mumtrans, elemtrans]

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
ZTT=file.Get(args.channel).Get("ZTT")
ZTT=file.Get(args.channel).Get("ZTT")
ZLL = file.Get(args.channel).Get("ZLL")
ST=file.Get(args.channel).Get("ST")
#GGTT=file.Get(args.channel).Get("GGTT")
ZTT.Add(ST.Clone())
#ZTT.Add(W.Clone())
Fake=file.Get(args.channel).Get("Fake")
'''
fData = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_data.root".format(year),"r")
hData = ROOT.TH1D(fData.Get(variables)) 
Data = ROOT.TH1D("Data","new hist of Data",var_used.nbins,var_used.binning)
for i in range(1, hData.GetNbinsX() + 1):
    new_bin_index = Data.FindBin(hData.GetBinCenter(i))
    #print(new_bin_index)
    Data.SetBinContent(new_bin_index, Data.GetBinContent(new_bin_index) + hData.GetBinContent(i))





fZTT = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_ZTT.root".format(year),"r")
hZTT = ROOT.TH1D(fZTT.Get(variables)) 
ZTT = ROOT.TH1D("ZTT","new hist of ZTT",var_used.nbins,var_used.binning)
for i in range(1, hZTT.GetNbinsX() + 1):
    new_bin_index = ZTT.FindBin(hZTT.GetBinCenter(i))
    ZTT.SetBinContent(new_bin_index, ZTT.GetBinContent(new_bin_index) + hZTT.GetBinContent(i))

fFake = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisSS/emu_{}_fake.root".format(year),"r")
hFake = ROOT.TH1D(fFake.Get(variables)) 
Fake = ROOT.TH1D("Fake","new hist of Fake",var_used.nbins,var_used.binning)
for i in range(1, hData.GetNbinsX() + 1):
    new_bin_index = Fake.FindBin(hFake.GetBinCenter(i))
    Fake.SetBinContent(new_bin_index, Fake.GetBinContent(new_bin_index) + hFake.GetBinContent(i))

fVV = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_VV.root".format(year),"r")
hVV = ROOT.TH1D(fVV.Get(variables))
VV = ROOT.TH1D("VV","new hist of VV",var_used.nbins,var_used.binning)
for i in range(1, hVV.GetNbinsX() + 1):
    new_bin_index = VV.FindBin(hVV.GetBinCenter(i))
    VV.SetBinContent(new_bin_index, VV.GetBinContent(new_bin_index) + hVV.GetBinContent(i))

fTop = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_Top.root".format(year),"r")
hTop = ROOT.TH1D(fTop.Get(variables)) 
Top = ROOT.TH1D("Top","new hist of Top",var_used.nbins,var_used.binning)
for i in range(1, hTop.GetNbinsX() + 1):
    new_bin_index = Top.FindBin(hData.GetBinCenter(i))
    Top.SetBinContent(new_bin_index, Top.GetBinContent(new_bin_index) + hTop.GetBinContent(i))

if "exclusive" in name:
    fGGWW = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_GGWW.root".format(year),"r")
    hGGWW = ROOT.TH1D(fGGWW.Get(variables)) 
    GGWW = ROOT.TH1D("GGWW","new hist of GGWW",var_used.nbins,var_used.binning)
    for i in range(1, hGGWW.GetNbinsX() + 1):
        new_bin_index = GGWW.FindBin(hData.GetBinCenter(i))
        GGWW.SetBinContent(new_bin_index, GGWW.GetBinContent(new_bin_index) + hGGWW.GetBinContent(i))


    fGGTT = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/mvisOS/emu_{}_GGTT.root".format(year),"r")
    hGGTT = ROOT.TH1D(fGGTT.Get(variables)) 
    GGTT = ROOT.TH1D("GGTT","new hist of GGTT",var_used.nbins,var_used.binning)
    for i in range(1, hGGTT.GetNbinsX() + 1):
        new_bin_index = GGTT.FindBin(hData.GetBinCenter(i))
        GGTT.SetBinContent(new_bin_index, GGTT.GetBinContent(new_bin_index) + hGGTT.GetBinContent(i))
    nGGWW = 0
    for i in range(1,GGWW.GetSize()+1):
        nGGWW += GGWW.GetBinContent(i)
    #print("nGGWW", nGGWW/10)
    nGGTT = 0
    for i in range(1,GGTT.GetSize()+1):
        nGGTT += GGTT.GetBinContent(i)
    #print("nGGTT", nGGTT/10)
    nZTT = 0
    for i in range(1,ZTT.GetSize()+1):
            nZTT += ZTT.GetBinContent(i)
    #print("nZTT", nZTT)
    nFake = 0
    for i in range(1,Fake.GetSize()+1):
        nFake += Fake.GetBinContent(i)
    #print("nFake", nFake)
    nVV = 0
    for i in range(1,VV.GetSize()+1):
        nVV += VV.GetBinContent(i)
    #print("nVV", nVV)
    nTop = 0
    for i in range(1,Top.GetSize()+1):
        nTop += Top.GetBinContent(i)
    #print("nTop", nTop) 
    nBKG = nZTT + nFake + nVV + nTop + nGGTT/10
    #print("nBKG", nBKG)
if name=="inclusive":
    Data.GetXaxis().SetTitle("")
    Data.GetXaxis().SetTitleSize(0)
    Data.GetXaxis().SetNdivisions(505)
elif "exclusive" in name:
    Data.GetXaxis().SetTitle(title)
    Data.GetXaxis().SetNdivisions(505)
    Data.GetXaxis().SetTitleSize(0.05)
    Data.GetXaxis().SetTitleOffset(1.1)
    Data.GetXaxis().SetLabelSize(0.04)
    Data.GetXaxis().SetTitleFont(42)

Data.GetYaxis().SetLabelFont(42)
Data.GetYaxis().SetLabelOffset(0.01)
if "inclusive" in name:
    Data.GetYaxis().SetLabelSize(0.06)
    Data.GetYaxis().SetTitleSize(0.075)
    Data.GetYaxis().SetTitleOffset(1.04)
elif "exclusive" in name:
    Data.GetYaxis().SetLabelSize(0.04)
    Data.GetYaxis().SetTitleSize(0.05)
    Data.GetYaxis().SetTitleOffset(1.5)
Data.SetTitle("")


#print(variables,type(variables))
if variables=="ptemu":
    #print("ptemu")
    Data.GetYaxis().SetTitle("Events/5GeV")
    #print("ptemu,ok")

if variables=="mvis":
    #print("mvis")
    Data.GetYaxis().SetTitle("Events/10GeV")
    #print("mvis,ok")

if variables=="elept" or variables=="mupt":
    #print("pt")
    Data.GetYaxis().SetTitle("Events/2GeV")
    #print("pt,ok")

if variables=="Acopl":
    #print("Acopl")
    Data.GetYaxis().SetTitle("Events/0.1")
    #print("Acopl,ok")

if variables=="elemtrans" or variables=="mumtrans":
    #print("mtrans")
    Data.GetYaxis().SetTitle("Events/5GeV")
    #print("mtrans,ok")

if variables=="MET":
    #print("MET")
    Data.GetYaxis().SetTitle("Events/5GeV")
    #print("MET,ok")

if variables=="eleeta" or variables=="mueta":
    #print("eta")
    Data.GetYaxis().SetTitle("Events/0.2")
    #print("eta,ok")

if variables=="deta":
    #print("deta")
    Data.GetYaxis().SetTitle("Events/0.1")
    #print("deta,ok")

if variables=="nTrk":
    #print("nTrk")
    Data.GetYaxis().SetTitle("Events/2")
    #print("nTrk,ok")
#Data.GetYaxis().SetTitle("Events/10GeV")
Data.SetMinimum(0.1)

#blind
if "exclusive" in name:
    for k in range(1,Data.GetSize()+1):
        Data.SetBinContent(k,0.0)


Data.SetMarkerStyle(20)
Data.SetMarkerSize(1)


VV.SetFillColor(ROOT.TColor.GetColor("#f6cd61"))
Fake.SetFillColor(ROOT.TColor.GetColor("#3da4ab"))
ZTT.SetFillColor(ROOT.TColor.GetColor("#969df1"))
Top.SetFillColor(ROOT.TColor.GetColor("#4a4e4d"))
if "exclusive" in name:
    GGWW.SetFillColor(ROOT.TColor.GetColor("#ff0000"))
    GGTT.SetFillColor(ROOT.TColor.GetColor("#00ff00"))


#ZTT.SetLineColor(1)
VV.SetLineColor(1)
Fake.SetLineColor(1)
ZTT.SetLineColor(1)
Top.SetLineColor(1)
Data.SetLineColor(1)
Data.SetLineWidth(2)

#GGTT.SetLineColor(2)
#GGTT.SetLineWidth(3)

stack=ROOT.THStack("stack","stack")
if "exclusive" in name:
    stack.Add(GGWW)
    stack.Add(GGTT)
stack.Add(VV)
stack.Add(Fake)
stack.Add(ZTT)
stack.Add(Top)

    




errorBand = VV.Clone()
if "exclusive" in name:
    errorBand.Add(GGWW)
    errorBand.Add(GGTT)
errorBand.Add(Fake)
errorBand.Add(ZTT)
errorBand.Add(Top)

errorBand.SetMarkerSize(0)
errorBand.SetFillColor(new_idx)
errorBand.SetFillStyle(3001)
errorBand.SetLineWidth(1)




if "exclusive" in name:
    pad1 = ROOT.TPad("pad1","pad1",0,0,1,1)
elif "inclusive" in name:
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
if "inclusive" in name:
    pad1.SetTopMargin(0.122)
    pad1.SetBottomMargin(0.026)
elif "exclusive" in name:
    pad1.SetTopMargin(0.122)
    pad1.SetBottomMargin(0.2)
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
    #legende.AddEntry(GGWW,"Signal(GG#rightarrow WW)x1e3","f")
elif "exclusive" in name:
    legende.AddEntry(GGWW,"Signal(GG#rightarrow WW)","f")
    legende.AddEntry(GGTT,"GG#rightarrow #tau#tau","f")
legende.AddEntry(VV,"VV","f")
legende.AddEntry(Fake,"Fake","f")
legende.AddEntry(ZTT,"Drell Yan","f")
legende.AddEntry(Top,"Top","f")
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
elif name=="exclusive01":
    c.SaveAs("Plotsemu/"+year+"exclusive01/signal_"+variables+".pdf")
    c.SaveAs("Plotsemu/"+year+"exclusive01/signal_"+variables+".png")