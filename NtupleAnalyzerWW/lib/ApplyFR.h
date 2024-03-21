#ifndef ApplyFR_H
#define ApplyFR_H
#include <ROOT/RDataFrame.hxx>
#include "TLorentzVector.h"

#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
#include "TMath.h"
#include <cmath>
#include "ROOT/RVec.hxx"
#include "ROOT/RDF/RInterface.hxx"
#include <vector>
#include <map>
using namespace std;
using namespace ROOT;
using namespace ROOT::VecOps;
using Vec_t = const ROOT::RVec<float>&;

class emuFR
{
    public:
    string yearconf;
    TH2D *WFR_allDM;
    TF1 *FRQCD_taupt_DM0;
    TF1 *FRQCD_lownTrk_DM0;
    TF1 *FRQCD_highnTrk_DM0;
    TF1 *FRQCD_taupt_DM1;
    TF1 *FRQCD_lownTrk_DM1;
    TF1 *FRQCD_highnTrk_DM1;
    TF1 *FRQCD_taupt_DM10;
    TF1 *FRQCD_lownTrk_DM10;
    TF1 *FRQCD_highnTrk_DM10;
    TF1 *FRQCD_taupt_DM11;
    TF1 *FRQCD_lownTrk_DM11;
    TF1 *FRQCD_highnTrk_DM11;
    TF1 *FRW_taupt_DM0;
    TF1 *FRW_lownTrk_DM0;
    TF1 *FRW_highnTrk_DM0;
    TF1 *FRW_taupt_DM1;
    TF1 *FRW_lownTrk_DM1;
    TF1 *FRW_highnTrk_DM1;
    TF1 *FRW_taupt_DM10;
    TF1 *FRW_lownTrk_DM10;
    TF1 *FRW_highnTrk_DM10;
    TF1 *FRW_taupt_DM11;
    TF1 *FRW_lownTrk_DM11;
    TF1 *FRW_highnTrk_DM11;
    TH1F *err_nt0_ffQCD;
    TH1F *err_nt0_ffW;
    float QCDxtrgSF;
    float WxtrgSF;
    mutauFR();
    mutauFR(string year);
};



//float GetFR_mutau(int taudecaymode, float mvis, float mtrans, float taupt, int nTrk, bool isMuonTauTrigger);
float GetFR_mutau_qcd(int taudecaymode, float taupt, int nTrk, bool isMuonTauTrigger,string year);
float GetFR_mutau_w(int taudecaymode, float taupt, int nTrk, bool isMuonTauTrigger, string year);
float Getwfraction(float mvis, float mtrans,string year);
float GetFR_mutau_qcd_sys_invertOS(float qcdFR,float FRratio);
float GetFR_mutau_w_sys_invertmT(float wFR,float FRratio);
float GetFR_mutau_qcd_sys_taupt(float qcdFR, float taupt, int decaymode, int taudecaymode, bool down);
float GetFR_mutau_w_sys_taupt(float wFR, float taupt, int decaymode, int taudecaymode, bool down);
float GetFR_mutau_qcd_sys_ntrk_dm(float qcdFR, int decaymode, int taudecaymode, bool down,string year);
float GetFR_mutau_w_sys_ntrk_dm(float qcdFR, int decaymode, int taudecaymode, bool down, string year);
float GetFR_mutau_qcd_sys_ntrk(float qcdFR, float FRratio);
float GetFR_mutau_w_sys_ntrk(float wFR, float FRratio);
float Getwfraction_sys(float wfraction, bool down);
float GetFR_mutau(float qcdFR, float wFR, float wfraction);






#endif