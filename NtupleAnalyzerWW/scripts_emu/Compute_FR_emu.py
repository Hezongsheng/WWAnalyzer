from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector, TCanvas, TH2D
import numpy as numpy
import sys
from math import cos, sin, sqrt, pi
import ROOT
import time as timer
from array import array
ROOT.EnableImplicitMT();
year = sys.argv[1]
print("Computing the OS-to-SS, antimu correction and the multiplied for year", year)
#sample = sys.argv[2]
#print("year is", year, "sample is", sample)

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat("1.2f")


postfixName=[""]
samplelist = ["data","VV","DY","top"]

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
'''
datalist = ["MuonEGA", "MuonEGB", "MuonEGC", "MuonEGD"]
DYlist = ["DYemu"]
toplist = ["TTToHadronic", "TTToSemiLeptonic", "TTTo2L2Nu_small", "ST_t_antitop", "ST_t_top", "ST_tW_antitop", "ST_tW_top"]
VVlist = ["WZ3Q2L", "WZ3LNu", "VV2L2Nu_0", "ZZ4L"]
ptlist = ["pte15to24_ptmu24to35", "pte15to24_ptmu35to45", "pte15to24_ptmugt45", "pte24to35_ptmu15to24", "pte24to35_ptmu24to35", "pte24to35_ptmu35to45", "pte24to35_ptmugt45", "pte35to45_ptmu15to24", "pte35to45_ptmu24to35", "pte35to45_ptmu35to45", "pte35to45_ptmugt45", "ptegt45_ptmu15to24", "ptegt45_ptmu24to35", "ptegt45_ptmu35to45", "ptegt45_ptmugt45"]
Sisolist = ["OSnn", "OSna", "OSan", "OSaa", "SSnn", "SSna", "SSan", "SSaa"]

for name in datalist:
    for Siso in Sisolist:
        for pt in ptlist:
            df = RDataFrame("Events", "/eos/user/z/zohe/WWdata/FR/ntuples_emu_{}_basicsel/{}{}_{}.root".format(year,name,Siso,pt)) 
            df = df.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight")
            total_sum = df.Sum("allweight").GetValue()
            print("ntuples_emu_{}_basicsel/{}_{}_{}.root".format(year,name,Siso,pt),total_sum)
'''



df_data = RDataFrame("Events","/eos/user/z/zohe/WWdata/FR/ntuples_emu_{}_basicsel/data.root".format(year))
df_VV = RDataFrame("Events","/eos/user/z/zohe/WWdata/FR/ntuples_emu_{}_basicsel/VV.root".format(year))
df_DY = RDataFrame("Events","/eos/user/z/zohe/WWdata/FR/ntuples_emu_{}_basicsel/DY.root".format(year))
df_top = RDataFrame("Events","/eos/user/z/zohe/WWdata/FR/ntuples_emu_{}_basicsel/top.root".format(year))
df_MC = RDataFrame("Events","/eos/user/z/zohe/WWdata/FR/ntuples_emu_{}_basicsel/MC.root".format(year))
dflist = [df_data, df_VV, df_DY, df_top, df_MC]
df_data = df_data.Define("allweight","float(1)")
df_VV = df_VV.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight*Acoweight*topptweight")
df_DY = df_DY.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight*Acoweight*topptweight")
df_top = df_top.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight*Acoweight*topptweight")
df_MC = df_MC.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight*Acoweight*topptweight")
'''
for df in [df_VV, df_MC]:
    df = df.Define("allweight","xsweight*puWeight*SFweight*L1PreFiringWeight_Nom*nPUtrkweight*nHStrkweight")
'''


pte_edges = [15, 24, 35, 45, 55]
ptmu_edges = [15, 24, 35, 45, 55]

def create_hist(df_f):
    h_f = df_f.Histo2D(("FR_weight", "FR_weight", len(pte_edges)-1, array('d', pte_edges), len(ptmu_edges)-1, array('d', ptmu_edges)), "elept", "mupt", "allweight")
    return h_f

def overflow2Dhist(h_FRweight):
    for i in range (1,h_FRweight.GetNbinsX()+1):
        overflow_ptmu = h_FRweight.GetBinContent(i,h_FRweight.GetNbinsY()) + h_FRweight.GetBinContent(i,h_FRweight.GetNbinsY()+1)
        h_FRweight.SetBinContent(i,h_FRweight.GetNbinsY(),overflow_ptmu)
    for i in range (1,h_FRweight.GetNbinsY()+1):
        overflow_pte = h_FRweight.GetBinContent(h_FRweight.GetNbinsX(),i) + h_FRweight.GetBinContent(h_FRweight.GetNbinsX()+1,i)
        h_FRweight.SetBinContent(h_FRweight.GetNbinsX(),i,overflow_pte)
    overflow_ptemu = h_FRweight.GetBinContent(h_FRweight.GetNbinsX(),h_FRweight.GetNbinsY()) + h_FRweight.GetBinContent(h_FRweight.GetNbinsX()+1,h_FRweight.GetNbinsY()+1)
    h_FRweight.SetBinContent(h_FRweight.GetNbinsX(), h_FRweight.GetNbinsY(), overflow_ptemu)
    return h_FRweight

def create_ratio(hist1, hist2):
    hist_ratio = hist1.Clone("hist_ratio")

    for i in range(1, hist_ratio.GetNbinsX() + 1):
        for j in range(1, hist_ratio.GetNbinsY() + 1):
            bin_content1 = hist1.GetBinContent(i, j)
            bin_content2 = hist2.GetBinContent(i, j)
            if bin_content2 != 0: 
                ratio = bin_content1 / bin_content2
            else:
                ratio = 0  
            hist_ratio.SetBinContent(i, j, ratio)
            #print(i, j, ratio)
    return hist_ratio


def create_diff(hist1, hist2):
    hist_diff = hist1.Clone("hist_ratio")

    for i in range(1, hist_diff.GetNbinsX() + 1):
        for j in range(1, hist_diff.GetNbinsY() + 1):
            bin_content1 = hist1.GetBinContent(i, j)
            bin_content2 = hist2.GetBinContent(i, j)
            diff = bin_content1 - bin_content2
            hist_diff.SetBinContent(i, j, diff)
            #print(i, j, diff)
    return hist_diff

def check_hist(hist_ratio):
    for i in range(1, hist_ratio.GetNbinsX() + 2):
        for j in range(1, hist_ratio.GetNbinsY() + 2):
            bin_content = hist_ratio.GetBinContent(i, j)
            print(i, j, bin_content)

'''
def display_num2D(c_f,h2d_f):
    for i in range(1,h2d_f.GetNbinsX()+1):
        for j in range(1,h2d_f.GetNbinsY()+1):
            content = h2d_f.GetBinContent(i, j)
            xCenter = h2d_f.GetXaxis().GetBinCenter(i);
            yCenter = h2d_f.GetYaxis().GetBinCenter(j);

            label = f"{content:.2f}"
            latex = ROOT.TLatex(xCenter, yCenter, label)
            latex.SetTextSize(0.02)
            latex.SetTextAlign(22)  # 居中对齐
            latex.Draw()
    c_f.Update()
'''        
    

    

fout = ROOT.TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/FR_{}.root".format(year),"recreate")

c=ROOT.TCanvas("canvas","",0,0,800,800)
c.SetRightMargin(0.15)

df_OSnaData = df_data.Filter("isOS").Filter("eleiso").Filter("muantiiso")
h_OSnaData = create_hist(df_OSnaData)
h_OSnaData = overflow2Dhist(h_OSnaData)
#print("OSnaData",h_OSnaData.GetBinContent(h_OSnaData.GetXaxis().FindBin(46),h_OSnaData.GetYaxis().FindBin(46)))
#print("OsnaData overflow")
#check_hist(h_OSnaData)

df_OSnaMC = df_MC.Filter("isOS").Filter("eleiso").Filter("muantiiso")
h_OSnaMC = create_hist(df_OSnaMC)
#print("MC")
#check_hist(h_OSnaMC)
h_OSnaMC = overflow2Dhist(h_OSnaMC)
#print("OSnaMC",h_OSnaMC.GetBinContent(h_OSnaMC.GetXaxis().FindBin(46),h_OSnaMC.GetYaxis().FindBin(46)))
#print("OSnaMC overflow")
#check_hist(h_OSnaMC)

df_OSnaVV = df_VV.Filter("isOS").Filter("eleiso").Filter("muantiiso")
h_OSnaVV = create_hist(df_OSnaVV)
##check_hist(h_OSnaVV)
h_OSnaVV = overflow2Dhist(h_OSnaVV)
#print("OSnaVV",h_OSnaVV.GetBinContent(h_OSnaVV.GetXaxis().FindBin(46),h_OSnaVV.GetYaxis().FindBin(46)))
#print("OSnaVV overflow")
#check_hist(h_OSnaVV)
#h_OSnaData.Add(h_OSnaVV, -1)

df_OSnatop = df_top.Filter("isOS").Filter("eleiso").Filter("muantiiso")
h_OSnatop = create_hist(df_OSnatop)
#print("top")
##check_hist(h_OSnatop)
h_OSnatop = overflow2Dhist(h_OSnatop)
#print("OSnatop",h_OSnatop.GetBinContent(h_OSnatop.GetXaxis().FindBin(46),h_OSnatop.GetYaxis().FindBin(46)))
#print("OSnatop overflow")
#check_hist(h_OSnatop)

#h_OSnaData.Add(h_OSnatop, -1)   
df_OSnaDY = df_DY.Filter("isOS").Filter("eleiso").Filter("muantiiso")   
h_OSnaDY = create_hist(df_OSnaDY)
#print("DY")
##check_hist(h_OSnaDY)
h_OSnaDY = overflow2Dhist(h_OSnaDY)
#print("OSnaDY",h_OSnaVV.GetBinContent(h_OSnaDY.GetXaxis().FindBin(46),h_OSnaDY.GetYaxis().FindBin(46)))
#print("OSnaDY overflow")
#check_hist(h_OSnaDY)
#h_OSnaData.Add(h_OSnaDY, -1)

#h_OSna = create_diff(h_OSnaData,h_OSnaMC)
#h_OSnaData1 = create_diff(h_OSnaData, h_OSnaVV)
#h_OSnaData2 = create_diff(h_OSnaData1, h_OSnatop)
#h_OSnaData3  = create_diff(h_OSnaData2, h_OSnaDY)
h_OSnaData = create_diff(h_OSnaData, h_OSnaMC)










df_SSnaData = df_data.Filter("!isOS").Filter("eleiso").Filter("muantiiso")
h_SSnaData = create_hist(df_SSnaData)
h_SSnaData = overflow2Dhist(h_SSnaData)
#print("SSnaData",h_SSnaData.GetBinContent(h_SSnaData.GetXaxis().FindBin(46),h_SSnaData.GetYaxis().FindBin(46)))
#print("SSnaData overflow")
#check_hist(h_SSnaData)

df_SSnaMC = df_MC.Filter("!isOS").Filter("eleiso").Filter("muantiiso")
h_SSnaMC = create_hist(df_SSnaMC)
h_SSnaMC = overflow2Dhist(h_SSnaMC)
#print("SSnaMC",h_SSnaMC.GetBinContent(h_SSnaMC.GetXaxis().FindBin(46),h_SSnaMC.GetYaxis().FindBin(46)))
#print("SSnaMC overflow")
#check_hist(h_SSnaMC)

df_SSnaVV = df_VV.Filter("!isOS").Filter("eleiso").Filter("muantiiso")
h_SSnaVV = create_hist(df_SSnaVV)
h_SSnaVV = overflow2Dhist(h_SSnaVV)
#print("SSnaVV",h_SSnaVV.GetBinContent(h_SSnaVV.GetXaxis().FindBin(46),h_SSnaVV.GetYaxis().FindBin(46)))
#print("SSnaVV overflow")
#check_hist(h_SSnaVV)
#h_SSnaData.Add(h_SSnaVV, -1)

df_SSnatop = df_top.Filter("!isOS").Filter("eleiso").Filter("muantiiso")
h_SSnatop = create_hist(df_SSnatop)
h_SSnatop = overflow2Dhist(h_SSnatop)
#print("SSnatop",h_SSnaData.GetBinContent(h_SSnatop.GetXaxis().FindBin(46),h_SSnatop.GetYaxis().FindBin(46)))
#print("SSnatop overflow")
#check_hist(h_SSnatop)
#h_SSnaData.Add(h_SSnatop, -1)

df_SSnaDY = df_DY.Filter("!isOS").Filter("eleiso").Filter("muantiiso")
h_SSnaDY = create_hist(df_SSnaDY)
h_SSnaDY = overflow2Dhist(h_SSnaDY)
#print("SSnaDY",h_SSnaDY.GetBinContent(h_SSnaDY.GetXaxis().FindBin(46),h_SSnaDY.GetYaxis().FindBin(46)))
#print("SSnaDY overflow")
#check_hist(h_SSnaDY)

#h_SSnaData.Add(h_SSnaDY, -1)
#h_SSna = create_diff(h_SSnaData,h_SSnaMC)
#h_na = create_ratio(h_OSna,h_SSna)
#h_SSnaData1 = create_diff(h_SSnaData, h_SSnaVV)
#h_SSnaData2 = create_diff(h_SSnaData1, h_SSnatop)
#h_SSnaData3 = create_diff(h_SSnaData2, h_SSnaDY)
h_SSnaData = create_diff(h_SSnaData, h_SSnaMC)
h_na = h_OSnaData
h_na.Divide(h_SSnaData)

#set the negative value in OS-to-SS to 0
for i in range(1,h_na.GetNbinsX()+1):
    for j in range(1,h_na.GetNbinsY()+1):
        if h_na.GetBinContent(i,j) < 0:
            h_na.SetBinContent(i,j,0)

c.cd()
h_na.SetTitle("")
h_na.SetName("OS-to-SS")
h_na.SetMarkerStyle(20)
h_na.SetMarkerColor(1)
h_na.SetLineColor(1)
h_na.GetXaxis().SetTitle("pt_{e}/GeV")
h_na.GetYaxis().SetTitle("pt_{\mu}/GeV")
h_na.GetZaxis().SetTitle("OS/SS weight")
h_na.Draw("zcol text")
lumi=add_lumi(year)
lumi.Draw("same")
cms=add_CMS()
cms.Draw("same")






fout.cd()
h_na.Write()

c.cd()
c.Modified()
c.SaveAs("OS-to-SS_"+year+".pdf")
c.SaveAs("OS-to-SS_"+year+".png")






#Create the OS/SS in an state
df_OSanData = df_data.Filter("isOS").Filter("eleantiiso").Filter("muiso")
h_OSanData = create_hist(df_OSanData)
h_OSanData = overflow2Dhist(h_OSanData)
df_OSanMC = df_MC.Filter("isOS").Filter("eleantiiso").Filter("muiso")
h_OSanMC = create_hist(df_OSanMC)
h_OSanMC = overflow2Dhist(h_OSanMC)
h_OSan = create_diff(h_OSanData,h_OSanMC)
df_SSanData = df_data.Filter("!isOS").Filter("eleantiiso").Filter("muiso")
h_SSanData = create_hist(df_SSanData)
h_SSanData = overflow2Dhist(h_SSanData)
df_SSanMC = df_MC.Filter("!isOS").Filter("eleantiiso").Filter("muiso")
h_SSanMC = create_hist(df_SSanMC)
h_SSanMC = overflow2Dhist(h_SSanMC)
h_SSan = create_diff(h_SSanData,h_SSanMC)
h_an = create_ratio(h_OSan,h_SSan)

#Create the OS/SS in aa state
df_OSaaData = df_data.Filter("isOS").Filter("eleantiiso").Filter("muantiiso")
h_OSaaData = create_hist(df_OSaaData)
h_OSaaData = overflow2Dhist(h_OSaaData)
df_OSaaMC = df_MC.Filter("isOS").Filter("eleantiiso").Filter("muantiiso")
h_OSaaMC = create_hist(df_OSaaMC)
h_OSaaMC = overflow2Dhist(h_OSaaMC)
h_OSaa = create_diff(h_OSaaData,h_OSaaMC)
df_SSaaData = df_data.Filter("!isOS").Filter("eleantiiso").Filter("muantiiso")
h_SSaaData = create_hist(df_SSaaData)
h_SSaaData = overflow2Dhist(h_SSaaData)
df_SSaaMC = df_MC.Filter("!isOS").Filter("eleantiiso").Filter("muantiiso")
h_SSaaMC = create_hist(df_SSaaMC)
h_SSaaMC = overflow2Dhist(h_SSaaMC)
h_SSaa = create_diff(h_SSaaData,h_SSaaMC)
h_aa = create_ratio(h_OSaa,h_SSaa)

h_antimuCor = create_ratio(h_an, h_aa)

c.cd()
h_antimuCor.SetTitle("")
h_antimuCor.SetName("antimuCor")
h_antimuCor.SetMarkerStyle(20)
h_antimuCor.SetMarkerColor(1)
h_antimuCor.SetLineColor(1)
h_antimuCor.GetXaxis().SetTitle("pt_{e}/GeV")
h_antimuCor.GetYaxis().SetTitle("pt_{\mu}/GeV")
h_antimuCor.GetZaxis().SetTitle("anti-#mu correction")
h_antimuCor.Draw("zcol text")
lumi=add_lumi(year)
lumi.Draw("same")
cms=add_CMS()
cms.Draw("same")

fout.cd()
h_antimuCor.Write()

c.cd()
c.Modified()
c.SaveAs("antimuCor_"+year+".pdf")
c.SaveAs("antimuCor_"+year+".png")

h_mul = h_na 
h_mul.Multiply(h_antimuCor)
c.cd()
h_mul.SetTitle("")
h_mul.SetName("antimuCor")
h_mul.SetMarkerStyle(20)
h_mul.SetMarkerColor(1)
h_mul.SetLineColor(1)
h_mul.GetXaxis().SetTitle("pt_{e}/GeV")
h_mul.GetYaxis().SetTitle("pt_{\mu}/GeV")
h_mul.GetZaxis().SetTitle("multiplied")
h_mul.Draw("zcol text")
lumi=add_lumi(year)
lumi.Draw("same")
cms=add_CMS()
cms.Draw("same")

c.cd()
c.Modified()
c.SaveAs("mul_"+year+".pdf")
c.SaveAs("mul_"+year+".png")
