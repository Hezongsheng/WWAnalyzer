#include "Correction.h"

spe_cor::spe_cor(string year){
    yearconf = year;
    if (year == "2016pre"){
        TFile* f_aco_fine=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/new_correction_acoplanarity_fine_2016pre.root","read");
        fit_aco_2030_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_2030_2030");
        fit_aco_3040_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_3040_2030");
        fit_aco_4050_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_2030");
        fit_aco_gt50_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_2030");
        fit_aco_3040_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_3040_3040");
        fit_aco_4050_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_3040");
        fit_aco_gt50_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_3040");
        fit_aco_4050_4050 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_4050");
        fit_aco_gt50_4050 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_4050");
        fit_aco_gt50_gt50 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_gt50");
        TFile* f_bs=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/beamspot_UL2016_preVFP_Data.root","read");
        h_bs_sigma = (TH1F*) f_bs->Get("bs_sigma");
        h_bs_z = (TH1F*) f_bs->Get("bs_z");
        TFile* f_bs_mc=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/beamspot_UL2016_preVFP_MC.root","read");
        h_bs_sigma_mc = (TH1F*) f_bs_mc->Get("bs_sigma");
        h_bs_z_mc = (TH1F*) f_bs_mc->Get("bs_z");
        bs_z_mc=h_bs_z_mc->GetMean();
        bs_zsigma_mc=h_bs_sigma_mc->GetMean();
        TFile *f_punt=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/corrs_ntracks_pu_UL2016_preVFP.root");
        correction_map=(TH2F*) f_punt->Get("corr");
        TFile *f_hsnt=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/corrs_ntracks_hs_UL2016_preVFP.root");
        correction_mapHS=(TH2F*) f_hsnt->Get("correction_map");
    }
    else if (year == "2016post"){
        TFile* f_aco_fine=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/new_correction_acoplanarity_fine_2016post.root","read");
        fit_aco_2030_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_2030_2030");
        fit_aco_3040_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_3040_2030");
        fit_aco_4050_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_2030");
        fit_aco_gt50_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_2030");
        fit_aco_3040_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_3040_3040");
        fit_aco_4050_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_3040");
        fit_aco_gt50_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_3040");
        fit_aco_4050_4050 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_4050");
        fit_aco_gt50_4050 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_4050");
        fit_aco_gt50_gt50 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_gt50");
        TFile* f_bs=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/beamspot_UL2016_postVFP_Data.root","read");
        h_bs_sigma = (TH1F*) f_bs->Get("bs_sigma");
        h_bs_z = (TH1F*) f_bs->Get("bs_z");
        TFile* f_bs_mc=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/beamspot_UL2016_postVFP_MC.root","read");
        h_bs_sigma_mc = (TH1F*) f_bs_mc->Get("bs_sigma");
        h_bs_z_mc = (TH1F*) f_bs_mc->Get("bs_z");
        bs_z_mc=h_bs_z_mc->GetMean();
        bs_zsigma_mc=h_bs_sigma_mc->GetMean();
        TFile *f_punt=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/corrs_ntracks_pu_UL2016_postVFP.root");
        correction_map=(TH2F*) f_punt->Get("corr");
        TFile *f_hsnt=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/corrs_ntracks_hs_UL2016_postVFP.root");
        correction_mapHS=(TH2F*) f_hsnt->Get("correction_map");
    }
    else if (year == "2017"){
        TFile* f_aco_fine=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/new_correction_acoplanarity_fine_2017.root","read");
        fit_aco_2030_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_2030_2030");
        fit_aco_3040_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_3040_2030");
        fit_aco_4050_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_2030");
        fit_aco_gt50_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_2030");
        fit_aco_3040_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_3040_3040");
        fit_aco_4050_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_3040");
        fit_aco_gt50_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_3040");
        fit_aco_4050_4050 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_4050");
        fit_aco_gt50_4050 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_4050");
        fit_aco_gt50_gt50 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_gt50");
        TFile* f_bs=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/beamspot_UL2017_Data.root","read");
        h_bs_sigma = (TH1F*) f_bs->Get("bs_sigma");
        h_bs_z = (TH1F*) f_bs->Get("bs_z");
        TFile* f_bs_mc=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/beamspot_UL2017_MC.root","read");
        h_bs_sigma_mc = (TH1F*) f_bs_mc->Get("bs_sigma");
        h_bs_z_mc = (TH1F*) f_bs_mc->Get("bs_z");
        bs_z_mc=h_bs_z_mc->GetMean();
        bs_zsigma_mc=h_bs_sigma_mc->GetMean();
        TFile *f_punt=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/corrs_ntracks_pu_UL2017.root");
        correction_map=(TH2F*) f_punt->Get("corr");
        TFile *f_hsnt=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/corrs_ntracks_hs_UL2017.root");
        correction_mapHS=(TH2F*) f_hsnt->Get("correction_map");
    }
    else if (year == "2018"){
        TFile* f_aco_fine=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/new_correction_acoplanarity_fine_2018.root","read");
        fit_aco_2030_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_2030_2030");
        fit_aco_3040_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_3040_2030");
        fit_aco_4050_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_2030");
        fit_aco_gt50_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_2030");
        fit_aco_3040_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_3040_3040");
        fit_aco_4050_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_3040");
        fit_aco_gt50_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_3040");
        fit_aco_4050_4050 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_4050");
        fit_aco_gt50_4050 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_4050");
        fit_aco_gt50_gt50 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_gt50");
        TFile* f_bs=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/beamspot_UL2018_Data.root","read");
        h_bs_sigma = (TH1F*) f_bs->Get("bs_sigma");
        h_bs_z = (TH1F*) f_bs->Get("bs_z");
        TFile* f_bs_mc=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/beamspot_UL2018_MC.root","read");
        h_bs_sigma_mc = (TH1F*) f_bs_mc->Get("bs_sigma");
        h_bs_z_mc = (TH1F*) f_bs_mc->Get("bs_z");
        bs_z_mc=h_bs_z_mc->GetMean();
        bs_zsigma_mc=h_bs_sigma_mc->GetMean();
        TFile *f_punt=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/corrs_ntracks_pu_UL2018.root");
        correction_map=(TH2F*) f_punt->Get("corr");
        TFile *f_hsnt=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/corrs_ntracks_hs_UL2018.root");
        correction_mapHS=(TH2F*) f_hsnt->Get("correction_map");
    }
    else {
        cout << "wrong year configuration" << endl;
    }
}

spe_cor::spe_cor(){
    
}
spe_cor spe_cor2016pre("2016pre");
spe_cor spe_cor2016post("2016post");
spe_cor spe_cor2017("2017");
spe_cor spe_cor2018("2018");

map<string, spe_cor> spe_cormap = {
    {"2016pre", spe_cor2016pre}, {"2016post", spe_cor2016post},{"2017", spe_cor2017},{"2018", spe_cor2018}
};


float GetGenAco(int nZGenCand, Vec_t &ZGenCand_phi, float Acopl){
    float genaco = 1.0;
    if (nZGenCand==2){//if we have 2 ZGenCand, we use genaco
        float dphi = TVector2::Phi_mpi_pi(ZGenCand_phi[0]-ZGenCand_phi[1]);
        genaco = 1-fabs(dphi)/TMath::Pi();
    }
    else{//else use recoaco
        genaco = Acopl;
    }
    return genaco;
}


float Get_Aweight(float gen_aco, int nZGenCand, Vec_t &ZGenCand_pt, float lep1pt, float lep2pt ,string year){
    float my_lep1pt = 0;
    float my_lep2pt = 0;
    if (nZGenCand==2){//if we have 2 ZGenCand, we use genpt
        my_lep1pt = TMath::Max(ZGenCand_pt[0],ZGenCand_pt[1]);
        my_lep2pt = TMath::Min(ZGenCand_pt[0],ZGenCand_pt[1]);
    }
    else{
        my_lep1pt = TMath::Max(lep1pt,lep2pt);
        my_lep2pt = TMath::Min(lep1pt,lep2pt);
    }
    float Acocut = 0.35;
    float A_weight=1.0;
    if (my_lep1pt<30 && my_lep2pt<30){
        A_weight = spe_cormap[year].fit_aco_2030_2030->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>30 && my_lep1pt<40 && my_lep2pt<30){
        A_weight = spe_cormap[year].fit_aco_3040_2030->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>40 && my_lep1pt<50 && my_lep2pt<30){
        A_weight = spe_cormap[year].fit_aco_4050_2030->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>50 && my_lep2pt<30){
        A_weight = spe_cormap[year].fit_aco_gt50_2030->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>30 && my_lep1pt<40 && my_lep2pt>30 && my_lep2pt<40 ){
        A_weight = spe_cormap[year].fit_aco_3040_3040->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>40 && my_lep1pt<50 && my_lep2pt>30 && my_lep2pt<40 ){
        A_weight = spe_cormap[year].fit_aco_4050_3040->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>50 && my_lep2pt>30 && my_lep2pt<40 ){
        A_weight = spe_cormap[year].fit_aco_gt50_3040->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>40 && my_lep1pt<50 && my_lep2pt>40 && my_lep2pt<50 ){
        A_weight = spe_cormap[year].fit_aco_4050_4050->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>50 && my_lep2pt>40 && my_lep2pt<50 ){
        A_weight = spe_cormap[year].fit_aco_gt50_4050->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>50 && my_lep2pt>50 ){
        A_weight = spe_cormap[year].fit_aco_gt50_gt50->Eval(TMath::Min(Acocut,gen_aco));
    }
    return A_weight;
}



ROOT::RVec<float> Get_BScor_ditaudz( Vec_t &PF_dz, ROOT::RVec<int> &PF_isMatchedToGenHS,float PV_z, float zvtxll,string year ){
    float bs_zsigma_obs=spe_cormap[year].h_bs_sigma->GetRandom();
    float bs_z_obs=spe_cormap[year].h_bs_z->GetRandom();
    float corr_zsig= (bs_zsigma_obs / spe_cormap[year].bs_zsigma_mc);
    float corr_z= bs_z_obs - corr_zsig * spe_cormap[year].bs_z_mc;

    auto mod = [PV_z, zvtxll,corr_z,corr_zsig](float dz, int HS ){
        float BScorrected_dz;
        if (HS==1){
            BScorrected_dz = fabs(PV_z+dz-zvtxll);
        }
        else{
            float z_corr = corr_z + corr_zsig * (PV_z+dz);
            BScorrected_dz = fabs(z_corr - zvtxll);
        }
        return BScorrected_dz;
    };
    ROOT::RVec<float> BScordz_ditaudz = Map(PF_dz,PF_isMatchedToGenHS,mod);
    return BScordz_ditaudz;
}

//Get Correction on n_putracks, apply to all simulation samples
//TFile *f_punt=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/npu_correction_2018.root");
//TH2F* correction_map=(TH2F*) f_punt->Get("correction_map");

float Get_ntpuweight(int ntpu, float zvtxll,string year){
    float zpos = zvtxll;
    if (zpos<-10) zpos=-9.99;
    else if (zpos>10) zpos=9.99;
    float ntpu_weight=spe_cormap[year].correction_map->GetBinContent(spe_cormap[year].correction_map->GetXaxis()->FindBin(TMath::Min(49,ntpu)),spe_cormap[year].correction_map->GetYaxis()->FindBin(zpos)); // where zvtxll is the ditau vertex z, and ntpu is the number of BS corrected PU tracks inside the window
    return ntpu_weight;
}

//Get Correction on NHS_tracks, apply only to DY and VV sample because they use the same generator
//TFile *f_hsnt=new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/corrections/nhs_correction_2018.root");
//TH2F* correction_mapHS=(TH2F*) f_hsnt->Get("correction_map");
float Get_ntHSweight(int ntracksHS, float gen_aco, string year){
    float nths_weight=spe_cormap[year].correction_mapHS->GetBinContent(spe_cormap[year].correction_mapHS->GetXaxis()->FindBin(TMath::Min(39,ntracksHS)),spe_cormap[year].correction_mapHS->GetYaxis()->FindBin(gen_aco));
    return nths_weight;
}




FR_weight::FR_weight(string year){
    yearconf = year;
    if (year == "2016pre"){
        TFile* f_FR = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/FR_2016pre.root","read");
        OStoSS = (TH2D*) f_FR->Get("OS-to-SS");
        antimuCor = (TH2D*) f_FR->Get("antimuCor");
        TFile* f_FRnTrk = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/FRnTrk_2016pre.root","read");
        OStoSSCor = (TH1D*) f_FRnTrk->Get("OS-to-SS_nTrkCor");
        antimuCorCor = (TH1D*) f_FRnTrk->Get("anti-mu_nTrkCor");
    }
    else if (year == "2016post"){
        TFile* f_FR = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/FR_2016post.root","read");
        OStoSS = (TH2D*) f_FR->Get("OS-to-SS");
        antimuCor = (TH2D*) f_FR->Get("antimuCor");
        TFile* f_FRnTrk = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/FRnTrk_2016post.root","read");
        OStoSSCor = (TH1D*) f_FRnTrk->Get("OS-to-SS_nTrkCor");
        antimuCorCor = (TH1D*) f_FRnTrk->Get("anti-mu_nTrkCor");
    }
    else if (year == "2017"){
        TFile* f_FR = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/FR_2017.root","read");
        OStoSS = (TH2D*) f_FR->Get("OS-to-SS");
        antimuCor = (TH2D*) f_FR->Get("antimuCor");
        TFile* f_FRnTrk = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/FRnTrk_2017.root","read");
        OStoSSCor = (TH1D*) f_FRnTrk->Get("OS-to-SS_nTrkCor");
        antimuCorCor = (TH1D*) f_FRnTrk->Get("anti-mu_nTrkCor");
    }
    else if (year == "2018"){
        TFile* f_FR = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/FR_2018.root","read");
        OStoSS = (TH2D*) f_FR->Get("OS-to-SS");
        antimuCor = (TH2D*) f_FR->Get("antimuCor");
        TFile* f_FRnTrk = new TFile("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/FRnTrk_2018.root","read");
        OStoSSCor = (TH1D*) f_FRnTrk->Get("OS-to-SS_nTrkCor");
        antimuCorCor = (TH1D*) f_FRnTrk->Get("anti-mu_nTrkCor");
    }
    else{
        cout<<"wrong year configuration"<<endl;
    }
}

FR_weight::FR_weight(){
    
}

FR_weight FR_weight2016pre("2016pre");
FR_weight FR_weight2016post("2016post");
FR_weight FR_weight2017("2017");
FR_weight FR_weight2018("2018");
map<string, FR_weight> FR_weightmap = {
    {"2016pre", FR_weight2016pre}, {"2016post", FR_weight2016post},{"2017", FR_weight2017}, {"2018", FR_weight2018}
};  

float Get_OStoSS(float elept, float mupt, string year){
    float OStoSS = 1.0;
    float elept_u = elept;
    float mupt_u = mupt;
    if (elept_u > 55) elept_u = 50;
    if (mupt_u > 55) mupt_u = 50;
    OStoSS = FR_weightmap[year].OStoSS->GetBinContent(FR_weightmap[year].OStoSS->GetXaxis()->FindBin(elept_u),FR_weightmap[year].OStoSS->GetYaxis()->FindBin(mupt_u));
    return OStoSS;
}

float Get_antimuCor(float elept, float mupt, string year){
    float antimuCor = 1.0;
    float elept_u = elept;
    float mupt_u = mupt;
    if (elept_u > 55) elept_u = 50;
    if (mupt_u > 55) mupt_u = 50;
    antimuCor = FR_weightmap[year].antimuCor->GetBinContent(FR_weightmap[year].antimuCor->GetXaxis()->FindBin(elept_u),FR_weightmap[year].antimuCor->GetYaxis()->FindBin(mupt_u));
    return antimuCor;
}


float Get_FRweight(float elept, float mupt, int nTrk, string year){
    float FRweight = 1.0;
    float elept_u = elept;
    float mupt_u = mupt;
    if (elept_u > 55) elept_u = 50;
    if (mupt_u > 55) mupt_u = 50;
    FRweight = FR_weightmap[year].OStoSS->GetBinContent(FR_weightmap[year].OStoSS->GetXaxis()->FindBin(elept_u),FR_weightmap[year].OStoSS->GetYaxis()->FindBin(mupt_u)) * FR_weightmap[year].antimuCor->GetBinContent(FR_weightmap[year].antimuCor->GetXaxis()->FindBin(elept_u),FR_weightmap[year].antimuCor->GetYaxis()->FindBin(mupt_u)) * FR_weightmap[year].OStoSSCor->GetBinContent(FR_weightmap[year].OStoSSCor->FindBin(nTrk)) * FR_weightmap[year].antimuCorCor->GetBinContent(FR_weightmap[year].antimuCorCor->FindBin(nTrk));
    
    return FRweight;
}


//For tt samples, get tt index
ROOT::RVec<int> Get_ttindex(ROOT::VecOps::RVec<int> &GenCand_id){
    int top_index = 0;
    int topbar_index = 0;
    //top id == 6, topbar id == -6. The minimum id corresponding to minimum lepton id 
    top_index = std::distance(GenCand_id.begin(),find(GenCand_id.begin(),GenCand_id.end(),6));
    topbar_index = std::distance(GenCand_id.begin(),find(GenCand_id.begin(),GenCand_id.end(),-6));
    ROOT::RVec<int> ttindex = {top_index, topbar_index};
    return ttindex;
}

float Get_topptCor(ROOT::RVec<int> Get_ttindex, ROOT::RVec<float> GenCand_pt){
    float toppt = GenCand_pt[Get_ttindex[0]];
    float topbarpt = GenCand_pt[Get_ttindex[1]];
    if (toppt > 500) toppt = 500;
    if (topbarpt > 500) topbarpt = 500;
    float topptCor = 1.0; 
    topptCor = TMath::Sqrt(TMath::Exp(0.0615 - 0.0005*toppt) * TMath::Exp(0.0615 - 0.0005*topbarpt));
    return topptCor;
}


