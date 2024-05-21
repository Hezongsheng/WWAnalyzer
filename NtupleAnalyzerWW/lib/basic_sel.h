#ifndef basic_sel_H
#define basic_sel_H

#include <ROOT/RDataFrame.hxx>
#include "TLorentzVector.h"

#include "TFile.h"
#include "TH1F.h"
#include "TH1D.h"
#include "TF1.h"
#include "TMath.h"
#include <cmath> 
#include <string>
#include <map>
#include "ROOT/RVec.hxx"
#include "ROOT/RDF/RInterface.hxx"
using namespace std;
using namespace ROOT;
using namespace ROOT::VecOps;

class musf
{
public:
    string yearconf;
    TH1F* h_muonRecoeff;
    TH1F* h_muonRecoeff_stat;
    TH1F* h_muonRecoeff_syst;
    TH2F* h_muonIsoSF;
    TH2F* h_muonIsoSF_stat;
    TH2F* h_muonIsoSF_syst;
    TH2F* h_muonIDSF;
    TH2F* h_muonIDSF_stat;
    TH2F* h_muonIDSF_syst;
    TH2F* h_muonTrgSF;
    TH2F* h_muonTrgSF_stat;
    TH2F* h_muonTrgSF_syst;
    TH2F* h_muonTrgSF_crosstrg;
    musf();
    musf(string year);
};

class elesf
{
    public:
    string yearconf;
    TH2F* h_eleRecoeffAbove20;
    TH2F* h_eleRecoeffBelow20;
    TH2F* h_eleIDSF;
    elesf();
    elesf(string year);
};

class trgsf
{
    public:
    string yearconf;
    TH2F* h_mu_trg24_data;
    TH2F* h_mu_trg24_zll;
    TH2F* h_mu_trg8_data;
    TH2F* h_mu_trg8_zll;
    TH2F* h_ele_trg24_data;
    TH2F* h_ele_trg24_zll;
    TH2F* h_ele_trg12_data;
    TH2F* h_ele_trg12_zll;
    trgsf();
    trgsf(string year);
};





class Getxsw_W
{
public:
    string yearconf;
    Getxsw_W();
    Getxsw_W(string year);
};

TLorentzVector GetLepVector(int Lepindex, ROOT::VecOps::RVec<Float_t> &LepCand_pt, ROOT::VecOps::RVec<Float_t> &LepCand_eta,ROOT::VecOps::RVec<Float_t> &LepCand_phi);

float GetMuonrecoSF(TLorentzVector my_mu, string year);
float GetMuonrecoSF_stat(TLorentzVector my_mu, string year);
float GetMuonrecoSF_syst(TLorentzVector my_mu, string year);
float GetMuonIsoSF(TLorentzVector my_mu, string year);
float GetMuonIsoSF_stat(TLorentzVector my_mu, string year);
float GetMuonIsoSF_syst(TLorentzVector my_mu, string year);
float GetMuonIDSF(TLorentzVector my_mu, string year);
float GetMuonIDSF_stat(TLorentzVector my_mu, string year);
float GetMuonIDSF_syst(TLorentzVector my_mu, string year);
float GetMuonTriggerSF(TLorentzVector my_mu, string year);
float GetMuonTriggerSF_stat(TLorentzVector my_mu, string year);
float GetMuonTriggerSF_syst(TLorentzVector my_mu, string year);
float GetMuonTriggerSF_crosstrg(TLorentzVector my_mu, string year);
float GetElerecoSF(TLorentzVector my_ele, string year);
float GetEleIDSF(TLorentzVector my_ele, string year);
float GetEffEleTrg24_Data(TLorentzVector my_ele, string year);
float GetEffEleTrg12_Data(TLorentzVector my_ele, string year);
float GetEffMuTrg24_Data(TLorentzVector my_mu, string year);
float GetEffMuTrg8_Data(TLorentzVector my_mu, string year);
float GetEffEleTrg24_Zll(TLorentzVector my_ele, string year);
float GetEffEleTrg12_Zll(TLorentzVector my_ele, string year);
float GetEffMuTrg24_Zll(TLorentzVector my_mu, string year);
float GetEffMuTrg8_Zll(TLorentzVector my_mu, string year);
float GetTrgSF(float eff_e_trg24_data, float eff_e_trg12_data, float eff_mu_trg24_data, float eff_mu_trg8_data, float eff_e_trg24_zll, float eff_e_trg12_zll, float eff_mu_trg24_zll, float eff_mu_trg8_zll, bool is_mu8ele23, bool is_mu23ele12);
float GetSFweight_emu(float murecosf, float muisosf,float muidsf, float elerecosf, float eleidsf, float trgsf);












ROOT::RVec<int> Getemuindex(int nLepCand, ROOT::VecOps::RVec<int> &LepCand_id, ROOT::VecOps::RVec<float> &LepCand_dz);

ROOT::RVec<int> Getmumuindex(int nLepCand, ROOT::VecOps::RVec<int> &LepCand_id, ROOT::VecOps::RVec<float> &LepCand_dz);

bool GetisOS(ROOT::VecOps::RVec<Int_t> &LepCand_charge, int lep1index, int lep2index);

float GetTransmass(TLorentzVector my_lep, float MET_pt, float MET_phi);

float GetCollMass(TLorentzVector my_lep1, TLorentzVector my_lep2, float MET_pt, float MET_phi);

float GetAcopl(TLorentzVector my_lep1, TLorentzVector my_lep2);

float recovtxz1(float lep1dz, float lep2dz, float PV_z);

float recovtxz2(TLorentzVector my_Lep1, TLorentzVector my_Lep2, float lep1dz, float lep2dz, float PV_z);

float recovtxz3(float lep1pt, float lep2pt, float lep1dz, float lep2dz, float PV_z);

float GeteeSF(ROOT::VecOps::RVec<Float_t> &GenCand_pt, ROOT::VecOps::RVec<Float_t> &GenCand_eta, ROOT::VecOps::RVec<Float_t> &GenCand_phi, int nTrk);




#endif