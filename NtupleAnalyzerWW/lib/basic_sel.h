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

float Getweight_Ctb(float weight_Ctb);

ROOT::RVec<int> Getemuindex(int nLepCand, ROOT::VecOps::RVec<int> &LepCand_id, ROOT::VecOps::RVec<float> &LepCand_dz);

bool GetisOS(ROOT::VecOps::RVec<Int_t> &LepCand_charge, int lep1index, int lep2index);

#endif