#include "basic_sel.h"

musf::musf(string year){
    yearconf = year;

}

musf::musf(){

}

musf musf2016pre("2016pre");
musf musf2016post("2016post");
musf musf2017("2017");
musf musf2018("2018");

map<string, musf> musfmap = {
    {"2016pre", musf2016pre}, {"2016post", musf2016post}, {"2017",musf2017}, {"2018", musf2018}
};

Getxsw_W::Getxsw_W(string year){
    yearconf = year;
    float luminosity = 59830.0;
    if (year == "2017"){
        luminosity = 41480.0;
    }
    if (year == "2016pre"){
        luminosity = 19520.0;
    }
    if (year == "2016post"){
        luminosity = 16810.0;
    }
    cout << "year = " << year << " lumi = " << luminosity << endl; 
}

Getxsw_W::Getxsw_W(){

}

Getxsw_W xs_W2016pre("2016pre");
Getxsw_W xs_W2016post("2016post");
Getxsw_W xs_W2017("2017");
Getxsw_W xs_W2018("2018");

map<string, Getxsw_W> xsw_Wmap = {
    {"2016pre", xs_W2016pre}, {"2016post", xs_W2016post},{"2017", xs_W2017},{"2018", xs_W2018}
};




//Get ele vector and mu vector
TLorentzVector GetLepVector(int Lepindex, ROOT::VecOps::RVec<Float_t> &LepCand_pt, ROOT::VecOps::RVec<Float_t> &LepCand_eta,ROOT::VecOps::RVec<Float_t> &LepCand_phi){
    TLorentzVector my_lep;
    my_lep.SetPtEtaPhiM(LepCand_pt[Lepindex],LepCand_eta[Lepindex],LepCand_phi[Lepindex],0);
    return my_lep;
}

float Getweight_Ctb(float weight_Ctb){
    return weight_Ctb;
}

//For emu final state, get emu index
ROOT::RVec<int> Getemuindex(int nLepCand, ROOT::VecOps::RVec<int> &LepCand_id, ROOT::VecOps::RVec<float> &LepCand_dz){
    int ele_index = 0;
    int mu_index = 0;
    //ele id == 11, mu id == 13. The minimum id corresponding to minimum lepton id 
    ele_index = ArgMin(LepCand_id);
    if (nLepCand == 2){
        mu_index = ArgMax(LepCand_id);
    }
    else{
        //Choose the lep id = 13 as our mu
        mu_index = std::distance(LepCand_id.begin(),find(LepCand_id.begin(),LepCand_id.end(),13));
    }
    ROOT::RVec<int> emuindex = {ele_index, mu_index};
    return emuindex;
}

bool GetisOS(ROOT::VecOps::RVec<Int_t> &LepCand_charge, int lep1index, int lep2index){
    if (LepCand_charge[lep1index]*LepCand_charge[lep2index]<0)
        return true;
    else
        return false;
}



