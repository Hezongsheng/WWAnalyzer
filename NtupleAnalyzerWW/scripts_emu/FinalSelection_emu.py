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
ROOT.gSystem.Load('/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/lib/RDFfunc.so')
ROOT.EnableImplicitMT();





### this code is used to perform basic selection on ntuples after nanoaod analyzer
### year: 2016pre, 2016post, 2017, 2018
### name: name of ntuple after analyzer
### sample: output root file name
year = sys.argv[1]
sample = sys.argv[2]
#name = sys.argv[3]

print ("year is ", year , type(year)," " , " sample is ", sample)


ngen = 0.
isdata = True
isW = False


#For W sample, we use genEventCount and don't consider genweight
#For others, we use genEventsSumw and consider genweight
if (sample=="W" or sample=="W1" or sample=="W2" or sample=="W3" or sample=="W4"):
    isW=True



if ("MuonEG" not in sample):
    isdata=False
    rdf2=0
    rdf2 = RDataFrame("Runs","/eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_emu_{}/{}.root".format(year,sample))
    ngen = rdf2.Sum("genEventSumw").GetValue()

print ("isdata ", isdata, " isW ", isW)
print ("ngen is ", ngen)
xs = 1.0
weight = 1.0
eff=1.0
luminosity = 59830.0
if (year=="2017"): luminosity=41480.0
if (year=="2016pre"): luminosity=19520.0
if (year=="2016post"): luminosity=16810.0

if (isdata):
    weight = 1.0






#xs eff need to be edited
if (sample=="DY"): 
    xs=6077.22 
    eff=0.318
    weight=luminosity*xs/ngen*eff
    
    
elif (sample=="TTTo2L2Nu"): 
    xs=791*0.1061
    eff=0.657
    weight=luminosity*xs/ngen*eff
    
elif (sample=="TTToSemiLeptonic" or "TTToSemiLeptonic" in sample): 
    xs=791*0.4392
    eff=0.401
    weight=luminosity*xs/ngen*eff
    
elif (sample=="TTToHadronic"):
    xs=791*0.4544
    eff=0.170
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ZZ2L2Nu"): 
    xs=3.0
    eff=0.302
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ZZ4L"): 
    xs=1.212 
    eff=0.304
    weight=luminosity*xs/ngen*eff

elif (sample=="ZZ2L2Q"): 
    xs=3.22 
    eff=0.373
    weight=luminosity*xs/ngen*eff
    
#elif (sample=="ZZ2Q2L"): 
#    xs=3.22 
#    eff=0.372686
#    weight=luminosity*xs/ngen*eff
    
elif (sample=="WZ2L2Q"): 
    xs=5.595 
    eff=0.341
    weight=luminosity*xs/ngen*eff

#elif (sample=="WZ2Q2L"): 
#    xs=5.595 
#    eff=0.340629667
#    weight=luminosity*xs/ngen*eff
    
elif (sample=="WW2L2Nu"): 
    xs=8.95
    eff=0.397
    weight=luminosity*xs/ngen*eff
    
elif (sample=="WZ3LNu"): 
    xs=4.42965
    eff=0.341
    weight=luminosity*xs/ngen*eff

elif (sample=="ST_tW_top"): 
    xs=39.65 
    eff=0.273
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ST_tW_antitop"): 
    xs=39.65 
    eff=0.272
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ST_t_top"): 
    xs=134.2
    eff=0.118
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ST_t_antitop"):
    xs=80.0 
    eff=0.122
    weight=luminosity*xs/ngen*eff
    
elif (sample=="GGTT"):
    xs = 1.161
    eff=0.008735
    weight=luminosity*xs/ngen*eff

#elif (sample=="GGTT_Ctb20"):
elif (sample=="GGToTauTau_Ctb20"):
    xs = 1.121
    eff= 0.0269
    weight=luminosity*xs/ngen*eff

elif (sample=="GGToWW"):
    xs = 0.00692
    eff = 0.368
    weight = luminosity*xs/ngen*eff


print ("cross section is ", xs, " eff is ", eff, " xsweight is ", weight)


df = RDataFrame(0)
df = RDataFrame("Events","/eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_emu_{}/{}.root".format(year,sample))
nentries = df.Count().GetValue()

print ("Before selection total entries", nentries)

#Define useful variable: e/mu index/pt/eta/phi/dz, isOS(emu is opposite sign), is_isolated

df_var = df.Define("emuindex","Getemuindex(nLepCand,LepCand_id, LepCand_dz)").Define("eleindex","emuindex[0]").Define("muindex","emuindex[1]")

df_var = df_var.Define("my_ele","GetLepVector(eleindex,LepCand_pt,LepCand_eta,LepCand_phi)")\
    .Define("my_mu","GetLepVector(muindex,LepCand_pt,LepCand_eta,LepCand_phi)")\
    .Define("elept","my_ele.Pt()").Define("eleeta","my_ele.Eta()").Define("elephi","my_ele.Phi()").Define("eledz","LepCand_dz[eleindex]")\
    .Define("mupt","my_mu.Pt()").Define("mueta","my_mu.Eta()").Define("muphi","my_mu.Phi()").Define("mudz","LepCand_dz[muindex]")\
    .Define("isOS","GetisOS(LepCand_charge,eleindex,muindex)")

df_sel = df_var.Filter("fabs(eleeta)<2.4 && fabs(mueta)<2.4").Filter("LepCand_muonMediumId[muindex]==1 && LepCand_muonIso[muindex]<0.20")\
    .Filter("my_ele.DeltaR(my_mu)>=0.5")



#Add information of mass (mvis>40, transverse mass, collinear mass), acoplanarity
df_var = df_sel.Define("mvis","(my_ele+my_mu).M()")\
    .Define("mumtrans","GetTransmass(my_mu, MET_pt, MET_phi)")\
    .Define("elemtrans","GetTransmass(my_ele, MET_pt, MET_phi)")\
    .Define("mcol","GetCollMass(my_ele, my_mu, MET_pt, MET_phi)").Define("Acopl","GetAcopl(my_ele,my_mu)")\
    .Define("x1","Getx1(my_ele, my_mu, MET_pt, MET_phi)")\
    .Define("x2","Getx2(my_ele, my_mu, MET_pt, MET_phi)")\
    .Define("sumM","GetsumM(my_ele, my_mu, MET_pt, MET_phi)")
df_sel = df_var.Filter("mvis>40")

#Define vtx with 3 definition (simple average, theta-average, pt-average),dzemu<0.1
df_addvtx = df_sel.Define("zvtxll1","recovtxz1(eledz, mudz,PV_z)")\
    .Define("zvtxll2","recovtxz2(my_ele, my_mu, eledz, mudz, PV_z)")\
    .Define("zvtxll3","recovtxz3(elept, mupt, eledz, mudz, PV_z)")\
    .Filter("fabs(eledz-mudz)<0.1")

df = df_addvtx.Define("genAco","-99.0").Define("Acoweight","1.0")




df = df.Define("Track_eleptdiff","Computediffpt_lep(Track_pt, elept)")\
    .Define("Track_eledeltaR","ComputedeltaR_lep(Track_eta, Track_phi, eleeta, elephi)")\
    .Define("Track_muptdiff","Computediffpt_lep(Track_pt, mupt)")\
    .Define("Track_mudeltaR","ComputedeltaR_lep(Track_eta, Track_phi, mueta, muphi)")\
    .Define("Track_elematch","Gettrkmatch(Track_eleptdiff,Track_eledeltaR)")\
    .Define("Track_mumatch","Gettrkmatch(Track_muptdiff,Track_mudeltaR)")









columns = ROOT.std.vector("string")()


for c in ("run","luminosityBlock","event","emuindex",\
    "my_ele","elept","eleeta","elephi","eledz",\
    "my_mu","mupt","mueta","muphi","mudz",\
    "isOS","mvis","mumtrans","elemtrans","mcol","Acopl",\
    "zvtxll1","zvtxll2","zvtxll3","genAco","Acoweight",\
    "MET_pt","MET_phi"
):
    columns.push_back(c)

if ("Ctb" in sample):
    columns.push_back("TauG2Weights_ceBRe_0p0")









df.Snapshot("Events","/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/{}.root".format(year,sample),columns)

nentries = df.Count().GetValue()
print("After selection entries", nentries)

time_end = timer.time()
print("totally cost",time_end-time_start)




