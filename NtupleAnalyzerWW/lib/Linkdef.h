#ifdef __CINT__

#pragma link C++ nestedclass;
#pragma link C++ nestedtypedef;

// includes all header files
#include "basic_sel.h"
#include "GetPFTrk.h"
#include "Correction.h"


// All classes
#pragma link C++ class musf+;
#pragma link C++ class Getxsw_W+;
#pragma link C++ class spe_cor;

//All functions
#pragma link C++ function GetLepVector Getemuindex Getmumuindex GetisOS GetTransmass GetCollMass GetAcopl recovtxz1 recovtxz2 recovtxz3;
#pragma link C++ function Computedz_lep Computediffpt_lep ComputedeltaR_lep Compute_ditau Gettrkmatch Getntrkcut_emu Getntrkcut_mumu;
#pragma link C++ function GetGenAco Get_Aweight Get_BScor_ditaudz Get_ntpuweight Get_ntHSweight;



#endif