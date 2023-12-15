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
    musf();
    musf(string year);
};

class Getxsw_W
{
public:
    string yearconf;
    Getxsw_W();
    Getxsw_W(string year);
};

TLorentzVector GetLepVector(int Lepindex, ROOT::VecOps::RVec<Float_t> &LepCand_pt, ROOT::VecOps::RVec<Float_t> &LepCand_eta,ROOT::VecOps::RVec<Float_t> &LepCand_phi);



ROOT::RVec<int> Getemuindex(int nLepCand, ROOT::VecOps::RVec<int> &LepCand_id, ROOT::VecOps::RVec<float> &LepCand_dz);

bool GetisOS(ROOT::VecOps::RVec<Int_t> &LepCand_charge, int lep1index, int lep2index);

float GetTransmass(TLorentzVector my_lep, float MET_pt, float MET_phi);

float GetCollMass(TLorentzVector my_lep1, TLorentzVector my_lep2, float MET_pt, float MET_phi);

float GetAcopl(TLorentzVector my_lep1, TLorentzVector my_lep2);

float recovtxz1(float lep1dz, float lep2dz, float PV_z);

float recovtxz2(TLorentzVector my_Lep1, TLorentzVector my_Lep2, float lep1dz, float lep2dz, float PV_z);

float recovtxz3(float lep1pt, float lep2pt, float lep1dz, float lep2dz, float PV_z);




#endif