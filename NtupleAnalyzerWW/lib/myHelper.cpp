#include "myHelper.h"

void WriteHistToFileEMu(TFile* myfile, std::vector<TH1F*> hist, std::string name, TString dir_name, TString uncertainties[35], TString fake_uncertainties[30], bool isMC, int nbhist, int nbhist_offset, int nbhistMC, bool write_uncertainties){
    TString postfix="";
    TDirectory *dir =myfile->mkdir(dir_name);
    dir->cd();
    if (!write_uncertainties) nbhist=1;
    bool do_write=true;
    bool is_iso = (dir_name=="em_0" or dir_name=="em_1" or dir_name=="em_2" or dir_name=="em_3" or dir_name=="em_4" or dir_name=="em_5" or dir_name=="em_6" or dir_name=="em_7" or dir_name=="em_8" or dir_name=="em_9" or dir_name=="em_10");
    for (int k=0; k<nbhist; k++){
        do_write=true;
        for (int j=0; j<hist[k]->GetSize()-1; j++){
            if (hist[k]->GetBinContent(j)<0) hist[k]->SetBinContent(j,0);
        }
        //include overflow in last bin
        hist[k]->SetBinContent(hist[k]->GetSize()-2,hist[k]->GetBinContent(hist[k]->GetSize()-2)+hist[k]->GetBinContent(hist[k]->GetSize()-1)); 
        hist[k]->SetBinError(hist[k]->GetSize()-2,pow(hist[k]->GetBinError(hist[k]->GetSize()-2)*hist[k]->GetBinError(hist[k]->GetSize()-2)+hist[k]->GetBinError(hist[k]->GetSize()-1)*hist[k]->GetBinError(hist[k]->GetSize()-1),0.5));
        hist[k]->SetBinContent(hist[k]->GetSize()-1,0);
        hist[k]->SetBinError(hist[k]->GetSize()-1,0);

        if (k<(nbhistMC+1-nbhist_offset)) postfix=uncertainties[k];
        else{ 
            postfix=fake_uncertainties[k-(nbhistMC+1-nbhist_offset)];
            if (is_iso) do_write=false;
        }
        hist[k]->SetName(name.c_str()+postfix);
        if (do_write) hist[k]->Write();
    }
}