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





### this code is used to perform basic selection on ntuples after nanoaod analyzer
### year: 2016pre, 2016post, 2017, 2018
### sample: output root file name
### inclusive or exclusive selection
year = sys.argv[1]
sample = sys.argv[2]
name = sys.argv[3]
category = sys.argv[4]

print ("year is ", year, " sample is ", sample, " name is ", name, " category is", category)


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

if (sample=="DYemu"):
    xs=2025.7*(0.178+0.174)*(0.178+0.174)
    eff=0.10687
    weight=luminosity*xs/ngen*eff
    
    
elif ("TTTo2L2Nu" in sample): 
    xs=791*0.1061
    eff=0.657
    weight=luminosity*xs/ngen*eff

    
elif ("TTToSemiLeptonic" in sample): 
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
    
elif (sample=="WZ2Q2L"): 
    xs=6.419 
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
    #xs = 1.121
    xs = 1.048
    #eff= 0.0269
    eff = 0.0403
    weight=luminosity*xs/ngen*eff

elif (sample=="GGToWW"):
    xs = 0.006561
    #eff = 0.368
    eff = 1.0
    weight = luminosity*xs/ngen*eff

elif ("VV2L2Nu" in sample):
    xs = 11.09 + 0.9738
    eff = 0.392
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
    .Define("isOS","GetisOS(LepCand_charge,eleindex,muindex)").Define("ptemu","(my_mu+my_ele).Pt()")
#if name=="exclusive":
#    df_var = df_var.Filter("ptemu>=40")

df_sel = df_var.Filter("fabs(eleeta)<2.5 && fabs(mueta)<2.4").Filter("LepCand_muonMediumId[muindex]==1").Filter("my_ele.DeltaR(my_mu)>=0.5")
if name=="exclusive" or name=="inclusive":
    df_sel = df_sel.Filter("LepCand_muonIso[muindex]<0.20").Filter("LepCand_eleMVAiso80[eleindex]==1")
elif name=="FR":
    df_sel = df_sel.Define("muiso","LepCand_muonIso[muindex]<0.20").Define("muantiiso","LepCand_muonIso[muindex]>=0.20 && LepCand_muonIso[muindex]<0.50").Define("eleiso","LepCand_eleMVAiso80[eleindex]==1").Define("eleantiiso","LepCand_eleMVAiso80[eleindex]==0 && LepCand_eleMVAisoL[eleindex]==1")


#Add Trigger
if year == "2016pre":
    df_sel = df_sel.Define("is_mu8ele23","(HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL) && (my_ele.Pt()>24) && (my_mu.Pt()>10)").Define("is_mu23ele12","(HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL) && (my_ele.Pt()>13) && (my_mu.Pt()>24)")
else: 
    df_sel = df_sel.Define("is_mu8ele23","(HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ) && (my_ele.Pt()>24) && (my_mu.Pt()>10)").Define("is_mu23ele12","(HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ) && (my_ele.Pt()>13) && (my_mu.Pt()>24)")

df_sel = df_sel.Filter("is_mu8ele23 || is_mu23ele12").Filter("my_ele.Pt()>15").Filter("my_mu.Pt()>15")



#Add xsweight and SFweight
if (not isdata):
    df_sel = df_sel.Define("murecosf","GetMuonrecoSF(my_mu,\"{}\")".format(year)).Define("murecosf_stat","GetMuonrecoSF_stat(my_mu,\"{}\")".format(year)).Define("murecosf_syst","GetMuonrecoSF_syst(my_mu,\"{}\")".format(year))\
        .Define("mutrgsf","GetMuonTriggerSF(my_mu,\"{}\")".format(year)).Define("mutrgsf_stat","GetMuonTriggerSF_stat(my_mu,\"{}\")".format(year)).Define("mutrgsf_syst","GetMuonTriggerSF_syst(my_mu,\"{}\")".format(year))\
        .Define("muidsf","GetMuonIDSF(my_mu,\"{}\")".format(year)).Define("muidsf_stat","GetMuonIDSF_stat(my_mu,\"{}\")".format(year)).Define("muidsf_syst","GetMuonIDSF_syst(my_mu,\"{}\")".format(year))\
        .Define("muisosf","GetMuonIsoSF(my_mu,\"{}\")".format(year)).Define("muisosf_stat","GetMuonIsoSF_stat(my_mu,\"{}\")".format(year)).Define("muisosf_syst","GetMuonIsoSF_syst(my_mu,\"{}\")".format(year))\
        .Define("elerecosf","GetElerecoSF(my_ele,\"{}\")".format(year)).Define("eleidsf","GetEleIDSF(my_ele,\"{}\")".format(year))\
        .Define("eff_ele_trg24_data","GetEffEleTrg24_Data(my_ele,\"{}\")".format(year)).Define("eff_ele_trg12_data","GetEffEleTrg12_Data(my_ele,\"{}\")".format(year))\
        .Define("eff_mu_trg24_data","GetEffMuTrg24_Data(my_mu,\"{}\")".format(year)).Define("eff_mu_trg8_data","GetEffMuTrg8_Data(my_mu,\"{}\")".format(year))\
        .Define("eff_ele_trg24_zll","GetEffEleTrg24_Zll(my_ele,\"{}\")".format(year)).Define("eff_ele_trg12_zll","GetEffEleTrg12_Zll(my_ele,\"{}\")".format(year))\
        .Define("eff_mu_trg24_zll","GetEffMuTrg24_Zll(my_mu,\"{}\")".format(year)).Define("eff_mu_trg8_zll","GetEffMuTrg8_Zll(my_mu,\"{}\")".format(year))\
        .Define("trgsf","GetTrgSF(eff_ele_trg24_data, eff_ele_trg12_data, eff_mu_trg24_data, eff_mu_trg8_data, eff_ele_trg24_zll, eff_ele_trg12_zll, eff_mu_trg24_zll, eff_mu_trg8_zll, is_mu8ele23, is_mu23ele12)")
    df_sel = df_sel.Define("xsweight","{}*genWeight".format(weight)).Define("SFweight","GetSFweight_emu(murecosf, muisosf, muidsf, elerecosf, eleidsf, trgsf)")
else:
    df_sel = df_sel.Define("murecosf","1.0").Define("murecosf_stat","1.0").Define("murecosf_syst","1.0")\
        .Define("mutrgsf","1.0").Define("mutrgsf_stat","1.0").Define("mutrgsf_syst","1.0")\
        .Define("muidsf","1.0").Define("muidsf_stat","1.0").Define("muidsf_syst","1.0")\
        .Define("muisosf","1.0").Define("muisosf_stat","1.0").Define("muisosf_syst","1.0")\
        .Define("elerecosf","1.0").Define("eleidsf","1.0")
    df_sel = df_sel.Define("xsweight","1.0").Define("SFweight","1.0")


#Add information of mass (mvis>40, transverse mass, collinear mass), acoplanarity
df_var = df_sel.Define("mvis","(my_ele+my_mu).M()")\
    .Define("mumtrans","GetTransmass(my_mu, MET_pt, MET_phi)")\
    .Define("elemtrans","GetTransmass(my_ele, MET_pt, MET_phi)")\
    .Define("mcol","GetCollMass(my_ele, my_mu, MET_pt, MET_phi)").Define("Acopl","GetAcopl(my_ele,my_mu)")
#df_sel = df_var.Filter("mvis>40")
df_sel = df_var




#Define vtx with 3 definition (simple average, theta-average, pt-average),dzemu<0.1
df_addvtx = df_sel.Define("zvtxll1","recovtxz1(eledz, mudz,PV_z)")\
    .Define("zvtxll2","recovtxz2(my_ele, my_mu, eledz, mudz, PV_z)")\
    .Define("zvtxll3","recovtxz3(elept, mupt, eledz, mudz, PV_z)")\
    .Filter("fabs(eledz-mudz)<0.1")

#Acoplanarity weights only for DY samples
if (isdata):
    df = df_addvtx.Define("genAco","float(-99)").Define("Acoweight","float(1)").Define("puWeight","1.0").Define("puWeightUp","1.0").Define("puWeightDown","1.0")
else:
    if category == "DY":
        df = df_addvtx.Define("genAco","GetGenAco(nGenCand, GenCand_phi, Acopl)").Define("Acoweight","Get_Aweight(genAco, nGenCand, GenCand_pt, elept, mupt, \"{}\")".format(year))
    elif category == "VV":
        df = df_addvtx.Define("genAco","GetGenAco(nGenCand, GenCand_phi, Acopl)").Define("Acoweight","float(1)")
    else:
        df = df_addvtx.Define("genAco","float(-99)").Define("Acoweight","float(1)")



#make new eletrack and mutrack collection
df = df.Define("Track_eleptdiff","Computediffpt_lep(Track_pt, elept)")\
    .Define("Track_eledeltaR","ComputedeltaR_lep(Track_eta, Track_phi, eleeta, elephi)")\
    .Define("Track_muptdiff","Computediffpt_lep(Track_pt, mupt)")\
    .Define("Track_mudeltaR","ComputedeltaR_lep(Track_eta, Track_phi, mueta, muphi)")\
    .Define("Track_elematch","Gettrkmatch(Track_eleptdiff,Track_eledeltaR)")\
    .Define("Track_mumatch","Gettrkmatch(Track_muptdiff,Track_mudeltaR)")

#Get ditaudz(putrk need to add BS correction and ditaudz is the trk distance to ditau vertex)
print("Calculate ditaudz")
if (isdata):
    df = df.Define("Track_ditaudz","Compute_ditaudz(Track_dz,PV_z,zvtxll1)")
else:
    df = df.Define("Track_ditaudz","Get_BScor_ditaudz(Track_dz,Track_isMatchedToHS,PV_z,zvtxll1,\"{}\")".format(year))

df = df.Define("Trkcut","Track_ditaudz<0.05 && (!Track_elematch) && (!Track_mumatch) && (Track_pt > 0.5) && abs(Track_eta) < 2.5")\
    .Define("nTrk","Sum(Trkcut)")\
    .Define("Trk_pt","Track_pt[Trkcut]")\
    .Define("Trk_eta","Track_eta[Trkcut]")\
    .Define("Trk_phi","Track_phi[Trkcut]")\
    .Define("Trk_dz","Track_dz[Trkcut]")\
    .Define("Trk_ditaudz","Track_ditaudz[Trkcut]")
df = df.Filter("nTrk<=100")

#Apply nputrack correction
print("Apply nputrack correctionz")
if (isdata):
    df = df.Define("nPUtrk","0")\
    .Define("nPUtrkweight","1.")
else:
    df = df.Define("PUtrkcut","Track_isMatchedToHS==0 && Trkcut==1")\
        .Define("nPUtrk","Sum(PUtrkcut)")\
        .Define("nPUtrkweight","Get_ntpuweight(nPUtrk, zvtxll1, \"{}\")".format(year))

#Apply nHStrk correction (only for DY and VV)
print("Apply nHStrack correctionz")
if (isdata):
    df = df.Define("nHStrk","0")\
        .Define("nHStrkweight","float(1)")
else:
    if (category == "DY" or category == "VV"):
        df = df.Define("HStrkcut","Track_isMatchedToHS==1 && Trkcut==1")\
            .Define("nHStrk","Sum(HStrkcut)")\
            .Define("nHStrkweight","Get_ntHSweight(nHStrk,genAco,\"{}\")".format(year))
    else:
        df = df.Define("HStrkcut","Track_isMatchedToHS==1 && Trkcut==1")\
            .Define("nHStrk","Sum(HStrkcut)")\
            .Define("nHStrkweight","float(1)")

if name == "exclusive":
    df = df.Filter("nTrk<=2")

if ("GGToWW" in sample or "GGToTauTau" in sample):
    df = df.Define("eeSF","GeteeSF(GenCand_pt, GenCand_eta, GenCand_phi, nTrk)")
else:
    df = df.Define("eeSF","float(1)")
 
if name == "exclusive" or name == "inclusive":
    df = df.Define("FRweight","Get_FRweight(elept, mupt, nTrk, \"{}\")".format(year))
    #df = df.Define("FRweight","float(1)")



uncertainties = ["","_CMS_pileup_yearDown","_CMS_pileup_yearUp","_CMS_emutrg_lowmuhighe_systDown","_CMS_emutrg_lowmuhighe_systUp","_CMS_emutrg_highmulowe_systDown","_CMS_emutrg_highmulowe_systUp","_CMS_emutrg_highmuhighe_systDown","_CMS_emutrg_highmuhighe_systUp","_CMS_elasticRescalingDown","_CMS_elasticRescalingUp","_CMS_L1PrefiringDown","_CMS_L1PrefiringUp","_CMS_muId_systDown","_CMS_muId_systUp","_CMS_muId_stat_yearDown","_CMS_muId_stat_yearUp","_CMS_muIso_systDown","_CMS_muIso_systUp","_CMS_muIso_stat_yearDown","_CMS_muIso_stat_yearUp","_CMS_elId_systDown","_CMS_elId_systUp","_CMS_ISRDown","_CMS_ISRUp","_CMS_FSRDown","_CMS_FSRUp","_CMS_PDFDown","_CMS_PDFUp","_CMS_muR0p5_muF0p5","_CMS_muRDown","_CMS_muFDown","_CMS_muFUp","_CMS_muRUp","_CMS_muR2p0_muF2p0"]

for k in range(23):
    if year=="2016pre":
        uncertainties[k]=uncertainties[k].replace("year","2016preVFP")
    elif year=="2016post":
        uncertainties[k]=uncertainties[k].replace("year","2016postVFP")
    elif year=="2017":
        uncertainties[k]=uncertainties[k].replace("year","2017")
    elif year=="2018":
        uncertainties[k]=uncertainties[k].replace("year","2018")

fake_uncertainties=["_CMS_fakebkg_emu_stat_pte15to24_ptmu24to35_yearDown","_CMS_fakebkg_emu_stat_pte15to24_ptmu24to35_yearUp","_CMS_fakebkg_emu_stat_pte15to24_ptmu35to45_yearDown","_CMS_fakebkg_emu_stat_pte15to24_ptmu35to45_yearUp","_CMS_fakebkg_emu_stat_pte15to24_ptmugt45_yearDown","_CMS_fakebkg_emu_stat_pte15to24_ptmugt45_yearUp","_CMS_fakebkg_emu_stat_pte24to35_ptmu15to24_yearDown","_CMS_fakebkg_emu_stat_pte24to35_ptmu15to24_yearUp","_CMS_fakebkg_emu_stat_pte24to35_ptmu24to35_yearDown","_CMS_fakebkg_emu_stat_pte24to35_ptmu24to35_yearUp","_CMS_fakebkg_emu_stat_pte24to35_ptmu35to45_yearDown","_CMS_fakebkg_emu_stat_pte24to35_ptmu35to45_yearUp","_CMS_fakebkg_emu_stat_pte24to35_ptmugt45_yearDown","_CMS_fakebkg_emu_stat_pte24to35_ptmugt45_yearUp","_CMS_fakebkg_emu_stat_pte35to45_ptmu15to24_yearDown","_CMS_fakebkg_emu_stat_pte35to45_ptmu15to24_yearUp","_CMS_fakebkg_emu_stat_pte35to45_ptmu24to35_yearDown","_CMS_fakebkg_emu_stat_pte35to45_ptmu24to35_yearUp","_CMS_fakebkg_emu_stat_pte35to45_ptmu35to45_yearDown","_CMS_fakebkg_emu_stat_pte35to45_ptmu35to45_yearUp","_CMS_fakebkg_emu_stat_pte35to45_ptmugt45_yearDown","_CMS_fakebkg_emu_stat_pte35to45_ptmugt45_yearUp","_CMS_fakebkg_emu_stat_ptegt45_ptmu15to24_yearDown","_CMS_fakebkg_emu_stat_ptegt45_ptmu15to24_yearUp","_CMS_fakebkg_emu_stat_ptegt45_ptmu24to35_yearDown","_CMS_fakebkg_emu_stat_ptegt45_ptmu24to35_yearUp","_CMS_fakebkg_emu_stat_ptegt45_ptmu35to45_yearDown","_CMS_fakebkg_emu_stat_ptegt45_ptmu35to45_yearUp","_CMS_fakebkg_emu_stat_ptegt45_ptmugt45_yearDown","_CMS_fakebkg_emu_stat_ptegt45_ptmugt45_yearUp"]

for k in range(30):
    if year=="2016pre":
        uncertainties[k]=fake_uncertainties[k].replace("year","2016preVFP")
    elif year=="2016post":
        uncertainties[k]=fake_uncertainties[k].replace("year","2016postVFP")
    elif year=="2017":
        uncertainties[k]=fake_uncertainties[k].replace("year","2017")
    elif year=="2018":
        uncertainties[k]=fake_uncertainties[k].replace("year","2018")

















columns = ROOT.std.vector("string")()


for c in ("run","luminosityBlock","event","emuindex",\
    "my_ele","elept","eleeta","elephi","eledz",\
    "my_mu","mupt","mueta","muphi","mudz",\
    "ptemu","isOS","mvis","mumtrans","elemtrans","mcol","Acopl","xsweight",\
    "zvtxll1","zvtxll2","zvtxll3","genAco","Acoweight",\
    "MET_pt","MET_phi",\
    "nGenCand","GenCand_id","GenCand_pt","GenCand_eta","GenCand_phi",\
    "puWeight","puWeightUp","puWeightDown",\
    "murecosf","murecosf_stat","murecosf_syst","muidsf","muidsf_stat","muidsf_syst","muisosf","muisosf_stat","muisosf_syst","mutrgsf","mutrgsf_stat","mutrgsf_syst","elerecosf","eleidsf","SFweight",\
    "nTrk","nPUtrk","nHStrk","nPUtrkweight","nHStrkweight",\
    "L1PreFiringWeight_Nom","L1PreFiringWeight_Up","L1PreFiringWeight_Dn","eeSF"
):
    columns.push_back(c)
if name=="FR":
    columns.push_back("muiso")
    columns.push_back("muantiiso")
    columns.push_back("eleiso")
    columns.push_back("eleantiiso")
if name=="exclusive" or name=="inclusive":
    columns.push_back("FRweight")

if ("GGToTauTau" in sample):
    columns.push_back("TauG2Weights_ceBRe_0p0")





if name == "exclusive":
    df.Snapshot("Events","/eos/user/z/zohe/WWdata/ntuples_emu_{}_basicsel/{}.root".format(year,sample),columns)
    nentries = df.Count().GetValue()
    print("After selection entries", nentries)
    time_end = timer.time()
    print("totally cost",time_end-time_start)
elif name == "inclusive":
    df.Snapshot("Events","/eos/user/z/zohe/WWdata/inclusive/ntuples_emu_{}_basicsel/{}.root".format(year,sample),columns)
elif name == "FR":
    df.Snapshot("Events","/eos/user/z/zohe/WWdata/FR/ntuples_emu_{}_basicsel/{}.root".format(year, sample),columns)