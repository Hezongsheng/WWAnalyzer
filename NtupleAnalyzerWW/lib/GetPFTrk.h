#ifndef GetPFTrk_H
#define GetPFTrk_H

#include <ROOT/RDataFrame.hxx>
#include "TLorentzVector.h"

#include "TFile.h"
#include "TH1F.h"
#include "TMath.h"
#include <cmath>
#include "TVector2.h"
#include "ROOT/RVec.hxx"
#include "ROOT/RDF/RInterface.hxx"
using namespace std;
using namespace ROOT;
using namespace ROOT::VecOps;

using Vec_t = const ROOT::RVec<float>&;


ROOT::RVec<float> Computedz_lep(Vec_t PF_dz, float lepdz);
ROOT::RVec<float> Computediffpt_lep(Vec_t PF_pt, float leppt);
ROOT::RVec<float> ComputedeltaR_lep(Vec_t PF_eta, Vec_t PF_phi, float lep_eta, float lep_phi);
ROOT::RVec<float> Compute_ditaudz(Vec_t trk_dz, float PV_z, float zvtxll);
ROOT::RVec<bool> Gettrkmatch(Vec_t Track_lepptdiff, Vec_t Track_lepdeltaR);
ROOT::RVec<int> Getntrkcut_emu(Vec_t ChargedPFCandidates_pt, Vec_t ChargedPFCandidates_eta, Vec_t ChargedPFCandidates_phi, Vec_t ChargedPFCandidates_dz,\
    Vec_t FinalEletrk_pt, Vec_t FinalEletrk_eta, Vec_t FinalEletrk_phi, Vec_t FinalEletrk_dz,\
    Vec_t FinalMuontrk_pt, Vec_t FinalMuontrk_eta, Vec_t FinalMuontrk_phi, Vec_t FinalMuontrk_dz);
ROOT::RVec<int> Gettrkcut_mumu(Vec_t ChargedPFCandidates_pt, Vec_t ChargedPFCandidates_eta, Vec_t ChargedPFCandidates_phi, Vec_t ChargedPFCandidates_dz,\
    Vec_t FinalMuontrk_pt, Vec_t FinalMuontrk_eta, Vec_t FinalMuontrk_phi, Vec_t FinalMuontrk_dz);

#endif
