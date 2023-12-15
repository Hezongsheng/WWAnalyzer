#include "GetPFTrk.h"

//compute the dz between lep and trk
ROOT::RVec<float> Computedz_lep(Vec_t PF_dz, float lepdz){
    auto mod = [lepdz](float dz){
        float deltadz = 0;
        if (lepdz==-99){
            deltadz = 99;
        }
        else{
            deltadz = fabs(dz-lepdz);
        }
        return deltadz;    };
    ROOT::RVec<float> dz_mu = Map(PF_dz,mod);
    return dz_mu;
} 

//Compute the difference of pt between lep and trk
ROOT::RVec<float> Computediffpt_lep(Vec_t PF_pt, float leppt){
    auto mod = [leppt](float pt){
        float ptdiff = 0;
        if (leppt==-99){
            ptdiff=99;
        }
        else{
            ptdiff = fabs(pt-leppt)/leppt;
        }
        return ptdiff;
    };
    ROOT::RVec<float> diffpt_lep = Map(PF_pt,mod);
    return diffpt_lep;
}

//Compute the deltaR between lep and trk
ROOT::RVec<float> ComputedeltaR_lep(Vec_t PF_eta, Vec_t PF_phi, float lep_eta, float lep_phi){
    auto mod = [lep_eta, lep_phi](float eta, float phi){
        float deltaR = 0;
        if (lep_eta==-99){
            deltaR = 99;
        }
        else{
            float dphi = TVector2::Phi_mpi_pi(lep_phi-phi);
            deltaR = sqrt((lep_eta-eta)*(lep_eta-eta) + dphi*dphi);
        }
        return deltaR;
    };
    ROOT::RVec<float> deltaR_lep = Map(PF_eta,PF_phi,mod);
    return deltaR_lep;
}


ROOT::RVec<float> Compute_ditaudz(Vec_t trk_dz, float PV_z, float zvtxll){
    auto mod = [PV_z, zvtxll](float dz){
        float ditaudz = dz+PV_z-zvtxll;
        return fabs(ditaudz);
    };
    ROOT::RVec<float> ditaudz = Map(trk_dz, mod);
    return ditaudz;
}


//To get known whether the trk is from lep, if the trk is from lep, return true
ROOT::RVec<bool> Gettrkmatch(Vec_t Track_lepptdiff, Vec_t Track_lepdeltaR){
    auto mod = [](float PF_lepptdiff, float PF_lepdeltaR){
        bool match = false;
        if (PF_lepptdiff < 0.1 && PF_lepdeltaR < 0.002){
            match = true;
        }
        return match;
    };
    ROOT::RVec<bool> trkmatch = Map(Track_lepptdiff,Track_lepdeltaR,mod);
    return trkmatch;
}


//To get known whether the trk is from ele or mu, if the trk is not from ele nor mu, return 1
ROOT::RVec<int> Getntrkcut_emu(Vec_t ChargedPFCandidates_pt, Vec_t ChargedPFCandidates_eta, Vec_t ChargedPFCandidates_phi, Vec_t ChargedPFCandidates_dz,\
    Vec_t FinalEletrk_pt, Vec_t FinalEletrk_eta, Vec_t FinalEletrk_phi, Vec_t FinalEletrk_dz,\
    Vec_t FinalMuontrk_pt, Vec_t FinalMuontrk_eta, Vec_t FinalMuontrk_phi, Vec_t FinalMuontrk_dz){
        auto mod = [FinalEletrk_pt,FinalEletrk_eta,FinalEletrk_phi,FinalEletrk_dz,\
            FinalMuontrk_pt, FinalMuontrk_eta, FinalMuontrk_phi, FinalMuontrk_dz](float PF_pt, float PF_eta, float PF_phi, float PF_dz){
                bool iseletrk = false;
                bool ismuontrk = false;

                if (FinalEletrk_pt.size()>0){
                    for (unsigned int i = 0; i < FinalEletrk_pt.size(); i++){
                        if (PF_pt==FinalEletrk_pt[i] && PF_eta==FinalEletrk_eta[i] && PF_phi==FinalEletrk_phi[i], PF_dz==FinalEletrk_dz[i])
                        iseletrk = true;
                    }
                }

                if (FinalMuontrk_pt.size()>0){
                    for (unsigned int i = 0; i < FinalMuontrk_pt.size(); i++){
                        if (PF_pt==FinalMuontrk_pt[i] && PF_eta==FinalMuontrk_eta[i] && PF_phi==FinalMuontrk_phi[i] && PF_dz==FinalMuontrk_dz[i])
                        ismuontrk = true;
                    }
                }

                if (iseletrk || ismuontrk){
                    return 0;
                }
                else{
                    return 1;
                }
            };
    ROOT::RVec<int> cut_excludeemu = Map(ChargedPFCandidates_pt, ChargedPFCandidates_eta, ChargedPFCandidates_phi, ChargedPFCandidates_dz, mod);
    return cut_excludeemu;    
}




//To get known whether the trk is from mu or mu, if the trk is not from mu, return 1
ROOT::RVec<int> Getntrkcut_mumu(Vec_t ChargedPFCandidates_pt, Vec_t ChargedPFCandidates_eta, Vec_t ChargedPFCandidates_phi, Vec_t ChargedPFCandidates_dz,\
    Vec_t FinalMuontrk_pt, Vec_t FinalMuontrk_eta, Vec_t FinalMuontrk_phi, Vec_t FinalMuontrk_dz){
        auto mod = [FinalMuontrk_pt, FinalMuontrk_eta, FinalMuontrk_phi, FinalMuontrk_dz](float PF_pt, float PF_eta, float PF_phi, float PF_dz){
            bool ismuontrk = false;

            if (FinalMuontrk_pt.size()>0){
                for (unsigned int i = 0; i < FinalMuontrk_pt.size(); i++){
                    if (PF_pt==FinalMuontrk_pt[i] && PF_eta==FinalMuontrk_eta[i] && PF_phi==FinalMuontrk_phi[i] && PF_dz==FinalMuontrk_dz[i])
                    ismuontrk = true;
                }
            }

            if (ismuontrk){
                return 0;
            }
            else{
                return 1;
            }
        };
    ROOT::RVec<int> cut_excludemumu = Map(ChargedPFCandidates_pt, ChargedPFCandidates_eta, ChargedPFCandidates_phi, ChargedPFCandidates_dz, mod);
    return cut_excludemumu;    
}

