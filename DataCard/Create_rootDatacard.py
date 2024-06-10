import ROOT

fout = ROOT.TFile("/eos/user/z/zohe/HiggsCombine/CMSSW_11_3_4/src/auxiliaries/shapes/ggww_emu_Run2.root", "RECREATE")
dir_em = fout.mkdir("em_01")

hist_names = ["VV", "Fake", "Top", "ZTT", "GGTT", "GGWW", "data"]

for hist_name in hist_names:
    fin = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_run2_basicsel/h_"+hist_name+".root", "READ")
    hist = fin.Get(hist_name)
    
    if hist:
        dir_em.cd()
        hist_clone = hist.Clone()
        if hist_name == "data":
            hist_clone.SetName("data_obs")
        hist_clone.Write()
    else:
        print("Histogram {} not found in {}".format(hist_name, fin.GetName()))
    fin.Close()

fout.Close()
