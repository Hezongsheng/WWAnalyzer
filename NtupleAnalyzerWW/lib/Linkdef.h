#ifdef __CINT__

#pragma link C++ nestedclass;
#pragma link C++ nestedtypedef;

// includes all header files
#include "basic_sel.h"
#include "GetPFTrk.h"
#include "Correction.h"
#include "myHelper.h"


// All classes
#pragma link C++ class musf+;
#pragma link C++ class elesf+;
#pragma link C++ class Getxsw_W+;
#pragma link C++ class spe_cor;
#pragma link C++ class FR_weight;

//All functions
#pragma link C++ function GetLepVector GetMuonrecoSF GetMuonrecoSF_stat GetMuonrecoSF_syst GetMuonIsoSF GetMuonIsoSF_stat GetMuonIsoSF_syst GetMuonIDSF GetMuonIDSF_stat GetMuonIDSF_syst GetMuonTriggerSF GetMuonTriggerSF_stat GetMuonTriggerSF_syst GetElerecoSF GetEleIDSF GetEffEleTrg24_Data GetEffEleTrg12_Data GetEffMuTrg24_Data GetEffMuTrg8_Data GetEffEleTrg24_Zll GetEffEleTrg12_Zll GetEffMuTrg24_Zll GetEffMuTrg8_Zll GetTrgSF GetSFweight_emu Getemuindex Getmumuindex GetisOS GetTransmass GetCollMass GetAcopl recovtxz1 recovtxz2 recovtxz3 GeteeSF;
#pragma link C++ function Computedz_lep Computediffpt_lep ComputedeltaR_lep Compute_ditau Gettrkmatch Getntrkcut_emu Getntrkcut_mumu;
#pragma link C++ function GetGenAco Get_Aweight Get_BScor_ditaudz Get_ntpuweight Get_ntHSweight Get_OStoSS Get_antimuCor Get_FRweight Get_ttindex Get_topptCor;
#pragma link C++ function WriteHistToFileEMu; 



#endif