#include "basic_sel.h"

musf::musf(string year){
    yearconf = year;
    if (year == "2016pre"){
        TFile *f_reco = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_reco_2016pre.root","READ");
        TFile *f_muonID= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2016_UL_HIPM_ID.root","read");
        TFile *f_muonIso= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2016_UL_HIPM_ISO.root","read");
        TFile *f_muonTrg= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2016_UL_HIPM_SingleMuonTriggers.root","read");
        TFile *f_muonTrg_crosstrg = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2016pre_HLTMu20Tau27.root","READ");
        h_muonRecoeff = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta");
        h_muonRecoeff_stat = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta_stat");
        h_muonRecoeff_syst = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta_syst");

        h_muonIsoSF= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt");
        h_muonIsoSF_stat= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt_stat");
        h_muonIsoSF_syst= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt_syst");

        h_muonIDSF= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt");
        h_muonIDSF_stat= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt_stat");
        h_muonIDSF_syst= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt_syst");

        h_muonTrgSF= (TH2F*)f_muonTrg->Get("NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt");
        h_muonTrgSF_stat= (TH2F*)f_muonTrg->Get("NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt_stat");
        h_muonTrgSF_syst= (TH2F*)f_muonTrg->Get("NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt_syst");
        h_muonTrgSF_crosstrg = (TH2F*) f_muonTrg_crosstrg->Get("SF2D");// xaxis: mupt, yaxis: fabs(mueta)
    }

    else if (year == "2016post"){
        TFile *f_reco = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_reco_2016post.root","READ");
        TFile *f_muonID= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2016_UL_ID.root","read");
        TFile *f_muonIso= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2016_UL_ISO.root","read");
        TFile *f_muonTrg= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2016_UL_SingleMuonTriggers.root","read");
        TFile *f_muonTrg_crosstrg = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2016post_HLTMu20Tau27.root","READ");
        h_muonRecoeff = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta");
        h_muonRecoeff_stat = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta_stat");
        h_muonRecoeff_syst = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta_syst");

        h_muonIsoSF= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt");
        h_muonIsoSF_stat= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt_stat");
        h_muonIsoSF_syst= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt_syst");

        h_muonIDSF= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt");
        h_muonIDSF_stat= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt_stat");
        h_muonIDSF_syst= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt_syst");

        h_muonTrgSF= (TH2F*)f_muonTrg->Get("NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt");
        h_muonTrgSF_stat= (TH2F*)f_muonTrg->Get("NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt_stat");
        h_muonTrgSF_syst= (TH2F*)f_muonTrg->Get("NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt_syst");
        h_muonTrgSF_crosstrg = (TH2F*) f_muonTrg_crosstrg->Get("SF2D");// xaxis: mupt, yaxis: fabs(mueta)
    }
    else if (year == "2017"){
        TFile *f_reco = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_reco_2017.root","READ");
        TFile *f_muonID= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2017_UL_ID.root","read");
        TFile *f_muonIso= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2017_UL_ISO.root","read");
        TFile *f_muonTrg= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2017_UL_SingleMuonTriggers.root","read");
        TFile *f_muonTrg_crosstrg = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2017_HLTMu20Tau27.root","READ");
        h_muonRecoeff = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta");
        h_muonRecoeff_stat = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta_stat");
        h_muonRecoeff_syst = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta_syst");

        h_muonIsoSF= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt");
        h_muonIsoSF_stat= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt_stat");
        h_muonIsoSF_syst= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt_syst");

        h_muonIDSF= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt");
        h_muonIDSF_stat= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt_stat");
        h_muonIDSF_syst= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt_syst");

        h_muonTrgSF= (TH2F*)f_muonTrg->Get("NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt");
        h_muonTrgSF_stat= (TH2F*)f_muonTrg->Get("NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt_stat");
        h_muonTrgSF_syst= (TH2F*)f_muonTrg->Get("NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt_syst");
        h_muonTrgSF_crosstrg = (TH2F*) f_muonTrg_crosstrg->Get("SF2D");// xaxis: mupt, yaxis: fabs(mueta)
    }
    else if (year == "2018"){
        TFile *f_reco = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_reco_2018.root","READ");
        TFile *f_muonID= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2018_UL_ID.root","read");
        TFile *f_muonIso= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2018_UL_ISO.root","read");
        TFile *f_muonTrg= new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/Efficiencies_muon_generalTracks_Z_Run2018_UL_SingleMuonTriggers.root","read");
        TFile *f_muonTrg_crosstrg = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2018_HLTMu20Tau27.root","READ");
        h_muonRecoeff = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta");
        h_muonRecoeff_stat = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta_stat");
        h_muonRecoeff_syst = (TH1F*)f_reco->Get("Efficiencies_muon_reco_abseta_syst");

        h_muonIsoSF= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt");
        h_muonIsoSF_stat= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt_stat");
        h_muonIsoSF_syst= (TH2F*)f_muonIso->Get("NUM_TightRelIso_DEN_MediumID_abseta_pt_syst");

        h_muonIDSF= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt");
        h_muonIDSF_stat= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt_stat");
        h_muonIDSF_syst= (TH2F*)f_muonID->Get("NUM_MediumID_DEN_TrackerMuons_abseta_pt_syst");

        h_muonTrgSF= (TH2F*)f_muonTrg->Get("NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt");
        h_muonTrgSF_stat= (TH2F*)f_muonTrg->Get("NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt_stat");
        h_muonTrgSF_syst= (TH2F*)f_muonTrg->Get("NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium_abseta_pt_syst");
        h_muonTrgSF_crosstrg = (TH2F*) f_muonTrg_crosstrg->Get("SF2D");// xaxis: mupt, yaxis: fabs(mueta)
    }
    else {
        cout << "wrong year configuration" << endl;
    }
}

musf::musf(){

}

musf musf2016pre("2016pre");
musf musf2016post("2016post");
musf musf2017("2017");
musf musf2018("2018");

map<string, musf> musfmap = {
    {"2016pre", musf2016pre}, {"2016post", musf2016post}, {"2017",musf2017}, {"2018", musf2018}
};

elesf::elesf(string year){
    yearconf = year;
    if (year == "2016pre"){
        TFile *f_recoAbove20 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi_ptAbove20.txt_EGM2D_UL2016preVFP.root","READ");
        TFile *f_recoBelow20 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi_ptBelow20.txt_EGM2D_UL2016preVFP.root","READ");
        TFile *f_eleID = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi.txt_Ele_wp80iso_preVFP_EGM2D.root","READ");
        h_eleRecoeffAbove20 = (TH2F*)f_recoAbove20->Get("EGamma_SF2D");
        h_eleRecoeffBelow20 = (TH2F*)f_recoBelow20->Get("EGamma_SF2D");
        h_eleIDSF = (TH2F*)f_eleID->Get("EGamma_SF2D");
    }
    else if (year == "2016post"){
        TFile *f_recoAbove20 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi_ptAbove20.txt_EGM2D_UL2016postVFP.root","READ");
        TFile *f_recoBelow20 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi_ptBelow20.txt_EGM2D_UL2016postVFP.root","READ");
        TFile *f_eleID = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi.txt_Ele_wp80iso_postVFP_EGM2D.root","READ");
        h_eleRecoeffAbove20 = (TH2F*)f_recoAbove20->Get("EGamma_SF2D");
        h_eleRecoeffBelow20 = (TH2F*)f_recoBelow20->Get("EGamma_SF2D");
        h_eleIDSF = (TH2F*)f_eleID->Get("EGamma_SF2D");
    }
    else if (year == "2017"){
        TFile *f_recoAbove20 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi_ptAbove20.txt_EGM2D_UL2017.root","READ");
        TFile *f_recoBelow20 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi_ptBelow20.txt_EGM2D_UL2017.root","READ");
        TFile *f_eleID = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi.txt_EGM2D_MVA80iso_UL17.root","READ");
        h_eleRecoeffAbove20 = (TH2F*)f_recoAbove20->Get("EGamma_SF2D");
        h_eleRecoeffBelow20 = (TH2F*)f_recoBelow20->Get("EGamma_SF2D");
        h_eleIDSF = (TH2F*)f_eleID->Get("EGamma_SF2D");
    }
    else if (year == "2018"){
        TFile *f_recoAbove20 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi_ptAbove20.txt_EGM2D_UL2018.root","READ");
        TFile *f_recoBelow20 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi_ptBelow20.txt_EGM2D_UL2018.root","READ");
        TFile *f_eleID = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/egammaEffi.txt_Ele_wp80iso_EGM2D.root","READ");
        h_eleRecoeffAbove20 = (TH2F*)f_recoAbove20->Get("EGamma_SF2D");
        h_eleRecoeffBelow20 = (TH2F*)f_recoBelow20->Get("EGamma_SF2D");
        h_eleIDSF = (TH2F*)f_eleID->Get("EGamma_SF2D");
    }
    else {
        cout << "wrong year configuration" << endl;
    }
}

elesf::elesf(){

}


elesf elesf2016pre("2016pre");
elesf elesf2016post("2016post");
elesf elesf2017("2017");
elesf elesf2018("2018");

map<string, elesf> elesfmap = {
    {"2016pre", elesf2016pre}, {"2016post", elesf2016post}, {"2017", elesf2017}, {"2018", elesf2018}
};


trgsf::trgsf(string year){
    yearconf = year;
    if (year == "2016pre"){
        TFile *f_mu_trg24 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2016pre_HLTMu23Ele12.root","read");
        TFile *f_mu_trg8 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2016pre_HLTMu8Ele23.root","read");
        TFile *f_ele_trg24 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_el_2016pre_HLTMu8Ele23.root","read");
        TFile *f_ele_trg12 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_el_2016pre_HLTMu23Ele12.root","read");
        h_mu_trg24_data = (TH2F*) f_mu_trg24->Get("eff_data");
        h_mu_trg24_zll = (TH2F*) f_mu_trg24->Get("eff_mc");
        h_mu_trg8_data = (TH2F*) f_mu_trg8->Get("eff_data");
        h_mu_trg8_zll = (TH2F*) f_mu_trg8->Get("eff_mc");
        h_ele_trg24_data = (TH2F*) f_ele_trg24->Get("eff_data");
        h_ele_trg24_zll = (TH2F*) f_ele_trg24->Get("eff_mc");
        h_ele_trg12_data = (TH2F*) f_ele_trg12->Get("eff_data");
        h_ele_trg12_zll = (TH2F*) f_ele_trg12->Get("eff_mc");
    }
    else if (year == "2016post"){
        TFile *f_mu_trg24 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2016post_HLTMu23Ele12.root","read");
        TFile *f_mu_trg8 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2016post_HLTMu8Ele23.root","read");
        TFile *f_ele_trg24 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_el_2016post_HLTMu8Ele23.root","read");
        TFile *f_ele_trg12 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_el_2016post_HLTMu23Ele12.root","read");
        h_mu_trg24_data = (TH2F*) f_mu_trg24->Get("eff_data");
        h_mu_trg24_zll = (TH2F*) f_mu_trg24->Get("eff_mc");
        h_mu_trg8_data = (TH2F*) f_mu_trg8->Get("eff_data");
        h_mu_trg8_zll = (TH2F*) f_mu_trg8->Get("eff_mc");
        h_ele_trg24_data = (TH2F*) f_ele_trg24->Get("eff_data");
        h_ele_trg24_zll = (TH2F*) f_ele_trg24->Get("eff_mc");
        h_ele_trg12_data = (TH2F*) f_ele_trg12->Get("eff_data");
        h_ele_trg12_zll = (TH2F*) f_ele_trg12->Get("eff_mc");
    }
    else if (year == "2017"){
        TFile *f_mu_trg24 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2017_HLTMu23Ele12.root","read");
        TFile *f_mu_trg8 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2017_HLTMu8Ele23.root","read");
        TFile *f_ele_trg24 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_el_2017_HLTMu8Ele23.root","read");
        TFile *f_ele_trg12 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_el_2017_HLTMu23Ele12.root","read");
        h_mu_trg24_data = (TH2F*) f_mu_trg24->Get("eff_data");
        h_mu_trg24_zll = (TH2F*) f_mu_trg24->Get("eff_mc");
        h_mu_trg8_data = (TH2F*) f_mu_trg8->Get("eff_data");
        h_mu_trg8_zll = (TH2F*) f_mu_trg8->Get("eff_mc");
        h_ele_trg24_data = (TH2F*) f_ele_trg24->Get("eff_data");
        h_ele_trg24_zll = (TH2F*) f_ele_trg24->Get("eff_mc");
        h_ele_trg12_data = (TH2F*) f_ele_trg12->Get("eff_data");
        h_ele_trg12_zll = (TH2F*) f_ele_trg12->Get("eff_mc");
    }
    else if (year == "2018"){
        TFile *f_mu_trg24 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2018_HLTMu23Ele12.root","read");
        TFile *f_mu_trg8 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_mu_2018_HLTMu8Ele23.root","read");
        TFile *f_ele_trg24 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_el_2018_HLTMu8Ele23.root","read");
        TFile *f_ele_trg12 = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scalefactors/sf_el_2018_HLTMu23Ele12.root","read");
        h_mu_trg24_data = (TH2F*) f_mu_trg24->Get("eff_data");
        h_mu_trg24_zll = (TH2F*) f_mu_trg24->Get("eff_mc");
        h_mu_trg8_data = (TH2F*) f_mu_trg8->Get("eff_data");
        h_mu_trg8_zll = (TH2F*) f_mu_trg8->Get("eff_mc");
        h_ele_trg24_data = (TH2F*) f_ele_trg24->Get("eff_data");
        h_ele_trg24_zll = (TH2F*) f_ele_trg24->Get("eff_mc");
        h_ele_trg12_data = (TH2F*) f_ele_trg12->Get("eff_data");
        h_ele_trg12_zll = (TH2F*) f_ele_trg12->Get("eff_mc");
    }
     else {
        cout << "wrong year configuration" << endl;
    }
}

trgsf::trgsf(){

}


trgsf trgsf2016pre("2016pre");
trgsf trgsf2016post("2016post");
trgsf trgsf2017("2017");
trgsf trgsf2018("2018");


map<string, trgsf> trgsfmap = {
    {"2016pre", trgsf2016pre}, {"2016post", trgsf2016post}, {"2017", trgsf2017}, {"2018", trgsf2018}
};










Getxsw_W::Getxsw_W(string year){
    yearconf = year;
    float luminosity = 0.0;
    if (year == "2018"){
        luminosity = 59740.0;
    }
    else if (year == "2017"){
        luminosity = 41480.0;
    }
    else if (year == "2016pre"){
        luminosity = 19520.0;
    }
    else if (year == "2016post"){
        luminosity = 16810.0;
    }
    cout << "year = " << year << " lumi = " << luminosity << endl; 
}

Getxsw_W::Getxsw_W(){

}

Getxsw_W xs_W2016pre("2016pre");
Getxsw_W xs_W2016post("2016post");
Getxsw_W xs_W2017("2017");
Getxsw_W xs_W2018("2018");

map<string, Getxsw_W> xsw_Wmap = {
    {"2016pre", xs_W2016pre}, {"2016post", xs_W2016post}, {"2017", xs_W2017}, {"2018", xs_W2018}
};




//Get ele vector and mu vector
TLorentzVector GetLepVector(int Lepindex, ROOT::VecOps::RVec<Float_t> &LepCand_pt, ROOT::VecOps::RVec<Float_t> &LepCand_eta,ROOT::VecOps::RVec<Float_t> &LepCand_phi){
    TLorentzVector my_lep;
    my_lep.SetPtEtaPhiM(LepCand_pt[Lepindex],LepCand_eta[Lepindex],LepCand_phi[Lepindex],0);
    return my_lep;
}

float GetMuonrecoSF(TLorentzVector my_mu, string year){
    float recosf = musfmap[year].h_muonRecoeff->GetBinContent(musfmap[year].h_muonRecoeff->GetXaxis()->FindBin(fabs(my_mu.Eta())));
    return recosf;
}
float GetMuonrecoSF_stat(TLorentzVector my_mu, string year){
    float recosf_stat = musfmap[year].h_muonRecoeff_stat->GetBinContent(musfmap[year].h_muonRecoeff_stat->GetXaxis()->FindBin(fabs(my_mu.Eta())));
    return recosf_stat;
}
float GetMuonrecoSF_syst(TLorentzVector my_mu, string year){
    float recosf_syst = musfmap[year].h_muonRecoeff_syst->GetBinContent(musfmap[year].h_muonRecoeff_syst->GetXaxis()->FindBin(fabs(my_mu.Eta())));
    return recosf_syst;
}


float GetMuonIsoSF(TLorentzVector my_mu, string year){
    float mu_pt=my_mu.Pt();
    if (mu_pt>120) mu_pt=119;
    if (mu_pt<15) mu_pt=16;
    float isosf= musfmap[year].h_muonIsoSF->GetBinContent(musfmap[year].h_muonIsoSF->GetXaxis()->FindBin(fabs(my_mu.Eta())),musfmap[year].h_muonIsoSF->GetYaxis()->FindBin(mu_pt));
    return isosf;
}

float GetMuonIsoSF_stat(TLorentzVector my_mu, string year){
    float mu_pt=my_mu.Pt();
    if (mu_pt>120) mu_pt=119;
    if (mu_pt<15) mu_pt=16;
    float isosf_stat = musfmap[year].h_muonIsoSF_stat->GetBinError(musfmap[year].h_muonIsoSF_stat->GetXaxis()->FindBin(fabs(my_mu.Eta())),musfmap[year].h_muonIsoSF_stat->GetYaxis()->FindBin(mu_pt));
    return isosf_stat;
}

float GetMuonIsoSF_syst(TLorentzVector my_mu, string year){
    float mu_pt=my_mu.Pt();
    if (mu_pt>120) mu_pt=119;
    if (mu_pt<15) mu_pt=16;
    float isosf_syst = musfmap[year].h_muonIsoSF_syst->GetBinError(musfmap[year].h_muonIsoSF_syst->GetXaxis()->FindBin(fabs(my_mu.Eta())),musfmap[year].h_muonIsoSF_syst->GetYaxis()->FindBin(mu_pt));
    return isosf_syst;
}


float GetMuonIDSF(TLorentzVector my_mu, string year){
    float mu_pt=my_mu.Pt();
    if (mu_pt>120) mu_pt=119;
    if (mu_pt<15) mu_pt=16;
    float idsf = musfmap[year].h_muonIDSF->GetBinContent(musfmap[year].h_muonIDSF->GetXaxis()->FindBin(fabs(my_mu.Eta())),musfmap[year].h_muonIDSF->GetYaxis()->FindBin(mu_pt));
    return idsf;
}

float GetMuonIDSF_stat(TLorentzVector my_mu, string year){
    float mu_pt=my_mu.Pt();
    if (mu_pt>120) mu_pt=119;
    if (mu_pt<15) mu_pt=16;
    float idsf_stat = musfmap[year].h_muonIDSF_stat->GetBinError(musfmap[year].h_muonIDSF_stat->GetXaxis()->FindBin(fabs(my_mu.Eta())),musfmap[year].h_muonIDSF_stat->GetYaxis()->FindBin(mu_pt));
    return idsf_stat;
}

float GetMuonIDSF_syst(TLorentzVector my_mu, string year){
    float mu_pt=my_mu.Pt();
    if (mu_pt>120) mu_pt=119;
    if (mu_pt<15) mu_pt=16;
    float idsf_syst = musfmap[year].h_muonIDSF_syst->GetBinError(musfmap[year].h_muonIDSF_syst->GetXaxis()->FindBin(fabs(my_mu.Eta())),musfmap[year].h_muonIDSF_syst->GetYaxis()->FindBin(mu_pt));
    return idsf_syst;
}


float GetMuonTriggerSF(TLorentzVector my_mu, string year){
    float mu_pt=my_mu.Pt();
    if (mu_pt>120) mu_pt=119;
    if (mu_pt<15) mu_pt=16;
    float trgsf = musfmap[year].h_muonTrgSF->GetBinContent(musfmap[year].h_muonTrgSF->GetXaxis()->FindBin(fabs(my_mu.Eta())),musfmap[year].h_muonTrgSF->GetYaxis()->FindBin(mu_pt));
    return trgsf;
}


float GetMuonTriggerSF_stat(TLorentzVector my_mu, string year){
    float mu_pt=my_mu.Pt();
    if (mu_pt>120) mu_pt=119;
    if (mu_pt<15) mu_pt=16;
    float trgsf_stat = musfmap[year].h_muonTrgSF_stat->GetBinError(musfmap[year].h_muonTrgSF_stat->GetXaxis()->FindBin(fabs(my_mu.Eta())),musfmap[year].h_muonTrgSF_stat->GetYaxis()->FindBin(mu_pt));
    return trgsf_stat;
}

float GetMuonTriggerSF_syst(TLorentzVector my_mu, string year){
    float mu_pt=my_mu.Pt();
    if (mu_pt>120) mu_pt=119;
    if (mu_pt<15) mu_pt=16;
    float trgsf_syst = musfmap[year].h_muonTrgSF_syst->GetBinError(musfmap[year].h_muonTrgSF_syst->GetXaxis()->FindBin(fabs(my_mu.Eta())),musfmap[year].h_muonTrgSF_syst->GetYaxis()->FindBin(mu_pt));
    return trgsf_syst;
}

float GetElerecoSF(TLorentzVector my_ele, string year){
    float ele_pt = my_ele.Pt();
    float recosf;
    if (ele_pt>500) ele_pt = 499;
    if (ele_pt<10) ele_pt = 10;
    if (ele_pt>=20){
        recosf = elesfmap[year].h_eleRecoeffAbove20->GetBinContent(elesfmap[year].h_eleRecoeffAbove20->GetXaxis()->FindBin(my_ele.Eta()),elesfmap[year].h_eleRecoeffAbove20->GetYaxis()->FindBin(ele_pt));
    }
    else{
        recosf = elesfmap[year].h_eleRecoeffBelow20->GetBinContent(elesfmap[year].h_eleRecoeffBelow20->GetXaxis()->FindBin(my_ele.Eta()),elesfmap[year].h_eleRecoeffBelow20->GetYaxis()->FindBin(ele_pt));
    }
    
    return recosf;
}

float GetEleIDSF(TLorentzVector my_ele, string year){
    float ele_pt = my_ele.Pt();
    if (ele_pt>500) ele_pt = 499;
    if (ele_pt<10) ele_pt = 11; 
    float idsf = elesfmap[year].h_eleIDSF->GetBinContent(elesfmap[year].h_eleIDSF->GetXaxis()->FindBin(my_ele.Eta()),elesfmap[year].h_eleIDSF->GetYaxis()->FindBin(ele_pt));
    return idsf;
}





float GetEffEleTrg24_Data(TLorentzVector my_ele, string year){
    float ele_pt = my_ele.Pt();
    if (ele_pt>200) ele_pt = 199;
    if (ele_pt<15) ele_pt = 15;
    float eff_ele_trg24_data = trgsfmap[year].h_ele_trg24_data->GetBinContent(trgsfmap[year].h_ele_trg24_data->GetXaxis()->FindBin(ele_pt),trgsfmap[year].h_ele_trg24_data->GetYaxis()->FindBin(fabs(my_ele.Eta())));
    return eff_ele_trg24_data;
}

float GetEffEleTrg12_Data(TLorentzVector my_ele, string year){
    float ele_pt = my_ele.Pt();
    if (ele_pt>200) ele_pt = 199;
    if (ele_pt<15) ele_pt = 15;
    float eff_ele_trg12_data = trgsfmap[year].h_ele_trg12_data->GetBinContent(trgsfmap[year].h_ele_trg12_data->GetXaxis()->FindBin(ele_pt),trgsfmap[year].h_ele_trg12_data->GetYaxis()->FindBin(fabs(my_ele.Eta())));
    return eff_ele_trg12_data;
}

float GetEffMuTrg24_Data(TLorentzVector my_mu, string year){
    float mu_pt = my_mu.Pt();
    if (mu_pt>200) mu_pt = 199;
    if (mu_pt<15) mu_pt = 15;
    float eff_mu_trg24_data = trgsfmap[year].h_mu_trg24_data->GetBinContent(trgsfmap[year].h_mu_trg24_data->GetXaxis()->FindBin(mu_pt),trgsfmap[year].h_mu_trg24_data->GetYaxis()->FindBin(fabs(my_mu.Eta())));
    return eff_mu_trg24_data;
}

float GetEffMuTrg8_Data(TLorentzVector my_mu, string year){
    float mu_pt = my_mu.Pt();
    if (mu_pt>200) mu_pt = 199;
    if (mu_pt<15) mu_pt = 15;
    float eff_mu_trg8_data = trgsfmap[year].h_mu_trg8_data->GetBinContent(trgsfmap[year].h_mu_trg8_data->GetXaxis()->FindBin(mu_pt),trgsfmap[year].h_mu_trg8_data->GetYaxis()->FindBin(fabs(my_mu.Eta())));
    return eff_mu_trg8_data;
}



float GetEffEleTrg24_Zll(TLorentzVector my_ele, string year){
    float ele_pt = my_ele.Pt();
    if (ele_pt>200) ele_pt = 199;
    if (ele_pt<15) ele_pt = 15;
    float eff_ele_trg24_zll = trgsfmap[year].h_ele_trg24_zll->GetBinContent(trgsfmap[year].h_ele_trg24_zll->GetXaxis()->FindBin(ele_pt),trgsfmap[year].h_ele_trg24_zll->GetYaxis()->FindBin(fabs(my_ele.Eta())));
    return eff_ele_trg24_zll;
}

float GetEffEleTrg12_Zll(TLorentzVector my_ele, string year){
    float ele_pt = my_ele.Pt();
    if (ele_pt>200) ele_pt = 199;
    if (ele_pt<15) ele_pt = 15;
    float eff_ele_trg12_zll = trgsfmap[year].h_ele_trg12_zll->GetBinContent(trgsfmap[year].h_ele_trg12_zll->GetXaxis()->FindBin(ele_pt),trgsfmap[year].h_ele_trg12_zll->GetYaxis()->FindBin(fabs(my_ele.Eta())));
    return eff_ele_trg12_zll;
}

float GetEffMuTrg24_Zll(TLorentzVector my_mu, string year){
    float mu_pt = my_mu.Pt();
    if (mu_pt>200) mu_pt = 199;
    if (mu_pt<15) mu_pt = 15;
    float eff_mu_trg24_zll = trgsfmap[year].h_mu_trg24_zll->GetBinContent(trgsfmap[year].h_mu_trg24_zll->GetXaxis()->FindBin(mu_pt),trgsfmap[year].h_mu_trg24_zll->GetYaxis()->FindBin(fabs(my_mu.Eta())));
    return eff_mu_trg24_zll;
}

float GetEffMuTrg8_Zll(TLorentzVector my_mu, string year){
    float mu_pt = my_mu.Pt();
    if (mu_pt>200) mu_pt = 199;
    if (mu_pt<15) mu_pt = 15;
    float eff_mu_trg8_zll = trgsfmap[year].h_mu_trg8_zll->GetBinContent(trgsfmap[year].h_mu_trg8_zll->GetXaxis()->FindBin(mu_pt),trgsfmap[year].h_mu_trg8_zll->GetYaxis()->FindBin(fabs(my_mu.Eta())));
    return eff_mu_trg8_zll;
}

float GetTrgSF(float eff_ele_trg24_data, float eff_ele_trg12_data, float eff_mu_trg24_data, float eff_mu_trg8_data, float eff_ele_trg24_zll, float eff_ele_trg12_zll, float eff_mu_trg24_zll, float eff_mu_trg8_zll, bool is_mu8ele23, bool is_mu23ele12){
    float probData =eff_ele_trg24_data*eff_mu_trg8_data*int(is_mu8ele23)+eff_mu_trg24_data*eff_ele_trg12_data*int(is_mu23ele12)-eff_ele_trg24_data*eff_mu_trg24_data*int(is_mu8ele23 && is_mu23ele12);
    float probMC =eff_ele_trg24_zll*eff_mu_trg8_zll*int(is_mu8ele23)+eff_mu_trg24_zll*eff_ele_trg12_zll*int(is_mu23ele12)-eff_ele_trg24_zll*eff_mu_trg24_zll*int(is_mu8ele23 && is_mu23ele12);
    float sf_trg = 1;
    if (probMC!=0){
        sf_trg=probData/probMC;
    }
    return sf_trg;
}







float GetSFweight_emu(float murecosf, float muisosf,float muidsf, float elerecosf, float eleidsf, float trgsf){
    float aweight=1.0;
    aweight = aweight*murecosf*muidsf*muisosf*elerecosf*eleidsf*trgsf;
    return aweight;
}














//For emu final state, get emu index
ROOT::RVec<int> Getemuindex(int nLepCand, ROOT::VecOps::RVec<int> &LepCand_id, ROOT::VecOps::RVec<float> &LepCand_dz){
    int ele_index = 0;
    int mu_index = 0;
    //ele id == 11, mu id == 13. The minimum id corresponding to minimum lepton id 
    ele_index = ArgMin(LepCand_id);
    if (nLepCand == 2){
        mu_index = ArgMax(LepCand_id);
    }
    else{
        //Choose the lep id = 13 as our mu
        mu_index = std::distance(LepCand_id.begin(),find(LepCand_id.begin(),LepCand_id.end(),13));
    }
    ROOT::RVec<int> emuindex = {ele_index, mu_index};
    return emuindex;
}


/*
//For mumu final state get mumu index
ROOT::RVec<int> Getmumuindex(int nLepCand, ROOT::VecOps::RVec<float> &LepCand_dz){
    int mu1index = 0;
    int mu2index = 0;
    if (nLepCand==2){
        mu1index = 0;
        mu2index = 1;
    }
    else{
        ROOT::VecOps::RVec<float> LepCand_Dz_sort = Sort(LepCand_dz);
        float mu1dz = LepCand_Dz_sort[0];
        float mu2dz = LepCand_Dz_sort[1];
        float dzdiff_min = mu2dz - mu1dz;
        for (int i = 2; i < int(LepCand_dz.size()); i++){
            if ((LepCand_Dz_sort[i] - LepCand_Dz_sort[i-1]) < dzdiff_min){
                mu1dz = LepCand_Dz_sort[i-1];
                mu2dz = LepCand_Dz_sort[i];
                dzdiff_min = mu2dz - mu1dz;
            }
        }
        mu1index = std::distance(LepCand_dz.begin(),find(LepCand_dz.begin(),LepCand_dz.end(),mu1dz));
        mu2index = std::instance(LepCand_dz.begin(),find(LepCand_dz.begin(),LepCand_dz.end(),mu2dz));
        if (mu1index > mu2index){
            int c = mu1index;
            mu1index = mu2index;
            mu2index = c;
        }
    }
    ROOT::RVec<int> mumuindex = {mu1index, mu2index};
    return mumuindex;
}
*/


//For mumu final state get mumu index
ROOT::RVec<int> Getmumuindex(int nLepCand, ROOT::VecOps::RVec<int> LepCand_id, ROOT::VecOps::RVec<float> &LepCand_dz){
    int mu1index = 0;
    int mu2index = 1;
    if (nLepCand != 2){
        ROOT::VecOps::RVec<int> indices;
        for (int i = 0; i < int(LepCand_id.size()); i++){
            if (LepCand_id[i] == 13){
                indices.push_back(i);
            }
        }
        mu1index = Min(indices);
        mu2index = Max(indices);
    }
    ROOT::RVec<int> mumuindex = {mu1index, mu2index};
    return mumuindex;
}



bool GetisOS(ROOT::VecOps::RVec<Int_t> &LepCand_charge, int lep1index, int lep2index){
    if (LepCand_charge[lep1index]*LepCand_charge[lep2index]<0)
        return true;
    else
        return false;
}

//calculate transverse mass
float GetTransmass(TLorentzVector my_lep, float MET_pt, float MET_phi){
    float lepMETdelphi = my_lep.Phi() - MET_phi;
    float mtrans = sqrt(2*my_lep.Pt()*MET_pt*(1-cos(lepMETdelphi)));
    return mtrans;
}

//calculate collinear mass in z direction
float GetCollMass(TLorentzVector my_lep1, TLorentzVector my_lep2, float MET_pt, float MET_phi){
    float metx = MET_pt * cos(MET_phi);
    float mety = MET_pt * sin(MET_phi) ;
    float m_mz_coll = 0;
    float x1 = ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px())) / ((my_lep1.Px()*my_lep2.Py())-(my_lep1.Py()*my_lep2.Px()) + (my_lep2.Py()*metx) - (my_lep2.Px()*mety));
    float x2 = ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px())) / ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px()) + (my_lep1.Px()*metx) - (my_lep1.Py()*metx));
    if ((x1*x2) > 0.){
        m_mz_coll = ((my_lep1+my_lep2).M()) / (sqrt(x1*x2));
    }
    return m_mz_coll;
}


//calculate acoplanarity
float GetAcopl(TLorentzVector my_lep1, TLorentzVector my_lep2){
    float delphi = my_lep1.DeltaPhi(my_lep2);
    float Acopl = 1 - fabs(delphi) / TMath::Pi();
    return Acopl;
}

//calculate the vtxz with promary method
float recovtxz1(float lep1dz, float lep2dz, float PV_z){
    float av_z = 0.5*(2*PV_z+lep1dz+lep2dz);
    return av_z;
}

//calculate the vtxz with the resolution in z
float recovtxz2(TLorentzVector my_Lep1, TLorentzVector my_Lep2, float lep1dz, float lep2dz, float PV_z){
    float theta1 = my_Lep1.Theta();
    float theta2 = my_Lep2.Theta();
    float z1 = lep1dz + PV_z;
    float z2 = lep2dz + PV_z;
    float sin2t1 = sin(theta1)*sin(theta1);
    float sin2t2 = sin(theta2)*sin(theta2);
    float zvtxll = (z1*sin2t1 + z2*sin2t2) / (sin2t1 + sin2t2);
    return zvtxll;
}

//calculate the vtxz with pt
float recovtxz3(float lep1pt, float lep2pt, float lep1dz, float lep2dz, float PV_z){
    float ptavdz = (lep1dz*lep1pt + lep2dz*lep2pt);
    float vtxz = ptavdz + PV_z;
    return vtxz;
}


float GeteeSF(ROOT::VecOps::RVec<Float_t> &GenCand_pt, ROOT::VecOps::RVec<Float_t> &GenCand_eta, ROOT::VecOps::RVec<Float_t> &GenCand_phi, int nTrk){
    float eeSF = 1.0;
    float ditaumass = 0;
    if (nTrk<=1){
        TLorentzVector gen_lep1, gen_lep2;
        gen_lep1.SetPtEtaPhiM(GenCand_pt[0],GenCand_eta[0],GenCand_phi[0],0);
        gen_lep2.SetPtEtaPhiM(GenCand_pt[1],GenCand_eta[1],GenCand_phi[1],0);
        ditaumass = (gen_lep1+gen_lep2).M();
        if (nTrk==0){
            eeSF = 2.02+0.00578 * ditaumass;
        }
        else{
            eeSF = 2.11+0.00361 * ditaumass;
        }
    }
    else {
        eeSF = 1.0;
    }
    return eeSF;
} 
