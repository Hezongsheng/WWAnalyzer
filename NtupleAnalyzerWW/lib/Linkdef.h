#ifdef __CINT__

#pragma link C++ nestedclass;
#pragma link C++ nestedtypedef;

// includes all header files
#include "basic_sel.h"
#include "GetPFTrk.h"


// All classes
#pragma link C++ class musf+;
#pragma link C++ class Getxsw_W+;

//All functions
#pragma link C++ function GetLepVector Getemuindex Getmumuindex GetisOS GetTransmass GetCollMass GetAcopl recovtxz1 recovtxz2 recovtxz3;
#pragma link C++ function Computedz_lep Computediffpt_lep ComputedeltaR_lep Compute_ditau Gettrkmatch Getntrkcut_emu Getntrkcut_mumu;



#endif