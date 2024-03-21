#include "ApplyFR.h"
using std::vector;

emuFR::emuFR(string year){
    yearconf = year;
    TFile *fFRw_mutau = new TFile(Form("/eos/user/z/zohe/WWAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/HistoforFR_%s/Wfractions.root",year.c_str()),"read");
    TFile *fFR_mutau = new TFile(Form("/eos/user/z/zohe/WWNanoAnalyzer/NtupleAnalyzerWW/scripts_emu/Histo/HistoforFR_%s/FRfit_emu.root",year.c_str()),"read");

    WFR_allDM = (TH2D*)fFRw_mutau->Get("frac_W");

    FRQCD_taupt_DM0 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM0_taupt");
    FRQCD_lownTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM0_lownTrk");
    FRQCD_highnTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM0_highnTrk");

    FRQCD_taupt_DM1 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM1_taupt");
    FRQCD_lownTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM1_lownTrk");
    FRQCD_highnTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM1_highnTrk");

    FRQCD_taupt_DM10 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM10_taupt");
    FRQCD_lownTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM10_lownTrk");
    FRQCD_highnTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM10_highnTrk");

    FRQCD_taupt_DM11 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM11_taupt");
    FRQCD_lownTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM11_lownTrk");
    FRQCD_highnTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM11_highnTrk");

    FRW_taupt_DM0 = (TF1*)fFR_mutau->Get("fitfunc_W_DM0_taupt");
    FRW_lownTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_W_DM0_lownTrk");
    FRW_highnTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_W_DM0_highnTrk");

    FRW_taupt_DM1 = (TF1*)fFR_mutau->Get("fitfunc_W_DM1_taupt");
    FRW_lownTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_W_DM1_lownTrk");
    FRW_highnTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_W_DM1_highnTrk");

    FRW_taupt_DM10 = (TF1*)fFR_mutau->Get("fitfunc_W_DM10_taupt");
    FRW_lownTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_W_DM10_lownTrk");
    FRW_highnTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_W_DM10_highnTrk");

    FRW_taupt_DM11 = (TF1*)fFR_mutau->Get("fitfunc_W_DM11_taupt");
    FRW_lownTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_W_DM11_lownTrk");
    FRW_highnTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_W_DM11_highnTrk");

    err_nt0_ffQCD = (TH1F*)fFR_mutau->Get("err_nt0_ffQCD");
    err_nt0_ffW = (TH1F*)fFR_mutau->Get("err_nt0_ffW");

    TH1F* h_tauFR_QCD_xtrg_SF = (TH1F*)fFR_mutau->Get("h_tauFR_QCD_xtrg_SF");
    TH1F* h_tauFR_W_xtrg_SF = (TH1F*)fFR_mutau->Get("h_tauFR_W_xtrg_SF");

    QCDxtrgSF = h_tauFR_QCD_xtrg_SF->GetBinContent(2)/h_tauFR_QCD_xtrg_SF->GetBinContent(3);
    WxtrgSF = h_tauFR_W_xtrg_SF->GetBinContent(2)/h_tauFR_W_xtrg_SF->GetBinContent(3);
    cout << year << " xtg SF " << " QCD: " << QCDxtrgSF << " W: " << WxtrgSF << endl;

}

mutauFR::mutauFR(){
    
}

mutauFR mutauFR2016pre("2016pre");
mutauFR mutauFR2016post("2016post");
mutauFR mutauFR2017("2017");
mutauFR mutauFR2018("2018");

map<string, mutauFR> mutauFRmap = {
    {"2016pre", mutauFR2016pre}, {"2016post", mutauFR2016post},{"2017", mutauFR2017},{"2018", mutauFR2018}
};





float GetFR_mutau_qcd(int taudecaymode, float taupt, int nTrk, bool isMuonTauTrigger, string year){
    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    int mynTrk=nTrk;
    if (nTrk>=100) mynTrk=99;
    float tfr_QCD=1.0;

    float ntrkcut = 25;
    if (taudecaymode==0 ){
        if (mynTrk<ntrkcut){
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM0->Eval(mytaupt)*mutauFRmap[year].FRQCD_lownTrk_DM0->Eval(mynTrk));
        }
        else{
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM0->Eval(mytaupt)*mutauFRmap[year].FRQCD_highnTrk_DM0->Eval(mynTrk));
        }

    }
    else if (taudecaymode==1){
        if (mynTrk<ntrkcut){
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM1->Eval(mytaupt)*mutauFRmap[year].FRQCD_lownTrk_DM1->Eval(mynTrk));
        }
        else{
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM1->Eval(mytaupt)*mutauFRmap[year].FRQCD_highnTrk_DM1->Eval(mynTrk));
        }
    }
    else if (taudecaymode==10){
        if (mynTrk<ntrkcut){
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM10->Eval(mytaupt)*mutauFRmap[year].FRQCD_lownTrk_DM10->Eval(mynTrk));
        }
        else{
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM10->Eval(mytaupt)*mutauFRmap[year].FRQCD_highnTrk_DM10->Eval(mynTrk));
        }

    }
    else if (taudecaymode==11){
        if (mynTrk<ntrkcut){
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM11->Eval(mytaupt)*mutauFRmap[year].FRQCD_lownTrk_DM11->Eval(mynTrk));
        }
        else{
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM11->Eval(mytaupt)*mutauFRmap[year].FRQCD_highnTrk_DM11->Eval(mynTrk));
        }
    }

    if (isMuonTauTrigger){
        tfr_QCD*=mutauFRmap[year].QCDxtrgSF;
    }
    return tfr_QCD;
}

float GetFR_mutau_w(int taudecaymode, float taupt, int nTrk, bool isMuonTauTrigger,string year){
    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    int mynTrk=nTrk;
    if (nTrk>=100) mynTrk=99;
    float tfr_W=1.0;

    float ntrkcut = 25;
    if (taudecaymode==0){
        if (mynTrk<ntrkcut){
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM0->Eval(mytaupt)*mutauFRmap[year].FRW_lownTrk_DM0->Eval(mynTrk));
        }
        else{
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM0->Eval(mytaupt)*mutauFRmap[year].FRW_highnTrk_DM0->Eval(mynTrk));
        }

    }
    else if (taudecaymode==1){
        if (mynTrk<ntrkcut){
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM1->Eval(mytaupt)*mutauFRmap[year].FRW_lownTrk_DM1->Eval(mynTrk));
        }
        else{
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM1->Eval(mytaupt)*mutauFRmap[year].FRW_highnTrk_DM1->Eval(mynTrk));
        }
    }
    else if (taudecaymode==10){
        if (mynTrk<ntrkcut){
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM10->Eval(mytaupt)*mutauFRmap[year].FRW_lownTrk_DM10->Eval(mynTrk));
        }
        else{
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM10->Eval(mytaupt)*mutauFRmap[year].FRW_highnTrk_DM10->Eval(mynTrk));
        }

    }
    else if (taudecaymode==11){
        if (mynTrk<ntrkcut){
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM11->Eval(mytaupt)*mutauFRmap[year].FRW_lownTrk_DM11->Eval(mynTrk));
        }
        else{
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM11->Eval(mytaupt)*mutauFRmap[year].FRW_highnTrk_DM11->Eval(mynTrk));
        }
    }

    if (isMuonTauTrigger){
        tfr_W*=mutauFRmap[year].WxtrgSF;
    }
    return tfr_W;
}


float Getwfraction(float mvis, float mtrans,string year){
    float fracW= 0;

    float mymvis = mvis;
    float mymtrans = mtrans;
    if (mymvis>300) mymvis=299;
    if (mymvis<50) mymvis=51;
    if (mymtrans>75) {
        fracW=1.0;
    }
    else{
        fracW = mutauFRmap[year].WFR_allDM->GetBinContent(mutauFRmap[year].WFR_allDM->GetXaxis()->FindBin(mymtrans),mutauFRmap[year].WFR_allDM->GetYaxis()->FindBin(mymvis));
    }
    return fracW;
}


//Inversion of selection criteria to measure the fake rates
float GetFR_mutau_qcd_sys_invertOS(float qcdFR,float FRratio){
    return qcdFR*FRratio;
}

float GetFR_mutau_w_sys_invertmT(float wFR,float FRratio){
    return wFR*FRratio;
}

//Extrapolation of the fake rates with tauh pT
float GetFR_mutau_qcd_sys_taupt(float qcdFR, float taupt, int decaymode, int taudecaymode, bool down){
    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    if (taudecaymode==decaymode){
        if (down){
            return qcdFR*(1-0.5*(mytaupt-30)/270);
        }
        else {
            return qcdFR*(1+0.5*(mytaupt-30)/270);
        }
    }
    else{
        return qcdFR;
    }
}

float GetFR_mutau_w_sys_taupt(float wFR, float taupt, int decaymode, int taudecaymode, bool down){
    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    if (taudecaymode==decaymode){
        if (down){
            return wFR*(1-0.5*(mytaupt-30)/270);
        }
        else {
            return wFR*(1+0.5*(mytaupt-30)/270);
        }
    }
    else{
        return wFR;
    }
}
//Statistical uncertainty in the Ntracks extrapolation
float GetFR_mutau_qcd_sys_ntrk_dm(float qcdFR, int decaymode, int taudecaymode, bool down,string year){
    float err = mutauFRmap[year].err_nt0_ffQCD->GetBinContent(decaymode+1);
    if (taudecaymode==decaymode){
        if (down){
            return qcdFR*(1-err);
        }
        else {
            return qcdFR*(1+err);
        }
    }
    else{
        return qcdFR;
    }
}

float GetFR_mutau_w_sys_ntrk_dm(float wFR, int decaymode, int taudecaymode, bool down,string year){
    float err = mutauFRmap[year].err_nt0_ffW->GetBinContent(decaymode+1);
    if (taudecaymode==decaymode){
        if (down){
            return wFR*(1-err);
        }
        else {
            return wFR*(1+err);
        }
    }
    else{
        return wFR;
    }
}

//Systematic uncertainty in the Ntracks extrapolation
float GetFR_mutau_qcd_sys_ntrk(float qcdFR, float FRratio){
    return qcdFR*FRratio;
}

float GetFR_mutau_w_sys_ntrk(float wFR, float FRratio){
    return wFR*FRratio;
}


//Systematic uncertainty of Determination of theWand QCD fractions //fix me
float Getwfraction_sys(float wfraction, bool down){
    if (wfraction>=1.0){
        return 1.0;
    }
    else{
        if (down){
            return 0.8*wfraction;
        }
        else{
            if (1.2*wfraction>=1.0){
                return 1.0;
            }
            else{
                return 1.2*wfraction;
            }
        }
    }
}



float GetFR_mutau(float qcdFR, float wFR, float wfraction){
    float tfr=wfraction*wFR + (1-wfraction)*qcdFR;
    return tfr;
}


