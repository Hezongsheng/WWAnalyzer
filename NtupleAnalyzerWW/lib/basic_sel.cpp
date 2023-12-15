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

//calculate transverse mass
float GetTransmass(TLorentzVector my_lep, float MET_pt, float MET_phi){
    float lepMETdelphi = my_lep.Phi() - MET_phi;
    float mtrans = sqrt(2*my_lep.Pt()*MET_pt*(1-cos(lepMETdelphi)));
    return mtrans;
}

//calculate collinear mass in z direction
float GetCollMass(TLorentzVector my_lep1, TLorentzVector my_lep2, float MET_pt, float MET_phi){
    float metx = MET_pt * cos(MET_phi);
    float mety = MET_pt * sin(MET_phi) ;
    float m_mz_coll = 0;
    float x1 = ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px())) / ((my_lep1.Px()*my_lep2.Py())-(my_lep1.Py()*my_lep2.Px()) + (my_lep2.Py()*metx) - (my_lep2.Px()*mety));
    float x2 = ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px())) / ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px()) + (my_lep1.Px()*metx) - (my_lep1.Py()*metx));
    if ((x1*x2) > 0.){
        m_mz_coll = ((my_lep1+my_lep2).M()) / (sqrt(x1*x2));
    }
    return m_mz_coll;
}

//calculate collinear mass in z direction
float Getx1(TLorentzVector my_lep1, TLorentzVector my_lep2, float MET_pt, float MET_phi){
    float metx = MET_pt * cos(MET_phi);
    float mety = MET_pt * sin(MET_phi) ;
    float m_mz_coll = 0;
    float x1 = ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px())) / ((my_lep1.Px()*my_lep2.Py())-(my_lep1.Py()*my_lep2.Px()) + (my_lep2.Py()*metx) - (my_lep2.Px()*mety));
    float x2 = ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px())) / ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px()) + (my_lep1.Px()*metx) - (my_lep1.Py()*metx));
    if ((x1*x2) > 0.){
        m_mz_coll = ((my_lep1+my_lep2).M()) / (sqrt(x1*x2));
    }
    return x1;
}



//calculate collinear mass in z direction
float Getx2(TLorentzVector my_lep1, TLorentzVector my_lep2, float MET_pt, float MET_phi){
    float metx = MET_pt * cos(MET_phi);
    float mety = MET_pt * sin(MET_phi) ;
    float m_mz_coll = 0;
    float x1 = ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px())) / ((my_lep1.Px()*my_lep2.Py())-(my_lep1.Py()*my_lep2.Px()) + (my_lep2.Py()*metx) - (my_lep2.Px()*mety));
    float x2 = ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px())) / ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px()) + (my_lep1.Px()*metx) - (my_lep1.Py()*metx));
    if ((x1*x2) > 0.){
        m_mz_coll = ((my_lep1+my_lep2).M()) / (sqrt(x1*x2));
    }
    return x2;
}

//calculate collinear mass in z direction
float GetsumM(TLorentzVector my_lep1, TLorentzVector my_lep2, float MET_pt, float MET_phi){
    float metx = MET_pt * cos(MET_phi);
    float mety = MET_pt * sin(MET_phi) ;
    float m_mz_coll = 0;
    float x1 = ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px())) / ((my_lep1.Px()*my_lep2.Py())-(my_lep1.Py()*my_lep2.Px()) + (my_lep2.Py()*metx) - (my_lep2.Px()*mety));
    float x2 = ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px())) / ((my_lep1.Px()*my_lep2.Py()) - (my_lep1.Py()*my_lep2.Px()) + (my_lep1.Px()*metx) - (my_lep1.Py()*metx));
    if ((x1*x2) > 0.){
        m_mz_coll = ((my_lep1+my_lep2).M()) / (sqrt(x1*x2));
    }
    return (my_lep1+my_lep2).M();
}












//calculate acoplanarity
float GetAcopl(TLorentzVector my_lep1, TLorentzVector my_lep2){
    float delphi = my_lep1.DeltaPhi(my_lep2);
    float Acopl = 1 - fabs(delphi) / TMath::Pi();
    return Acopl;
}

//calculate the vtxz with promary method
float recovtxz1(float lep1dz, float lep2dz, float PV_z){
    float av_z = 0.5*(2*PV_z+lep1dz+lep2dz);
    return av_z;
}

//calculate the vtxz with the resolution in z
float recovtxz2(TLorentzVector my_Lep1, TLorentzVector my_Lep2, float lep1dz, float lep2dz, float PV_z){
    float theta1 = my_Lep1.Theta();
    float theta2 = my_Lep2.Theta();
    float z1 = lep1dz + PV_z;
    float z2 = lep2dz + PV_z;
    float sin2t1 = sin(theta1)*sin(theta1);
    float sin2t2 = sin(theta2)*sin(theta2);
    float zvtxll = (z1*sin2t1 + z2*sin2t2) / (sin2t1 + sin2t2);
    return zvtxll;
}

//calculate the vtxz with pt
float recovtxz3(float lep1pt, float lep2pt, float lep1dz, float lep2dz, float PV_z){
    float ptavdz = (lep1dz*lep1pt + lep2dz*lep2pt);
    float vtxz = ptavdz + PV_z;
    return vtxz;
}



