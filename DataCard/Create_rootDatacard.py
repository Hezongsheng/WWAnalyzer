import ROOT
import sys

name = sys.argv[1]
if name == "nTrk0":
    fout = ROOT.TFile("/eos/user/z/zohe/HiggsCombine/CMSSW_11_3_4/src/auxiliaries/shapes/ggww_emu_Run2.root", "UPDATE")
    #dir_em = fout.mkdir("em_0")
    dir_em = fout.GetDirectory("em_0")
elif name == "nTrk1":
    fout = ROOT.TFile("/eos/user/z/zohe/HiggsCombine/CMSSW_11_3_4/src/auxiliaries/shapes/ggww_emu_Run2.root", "UPDATE")
    #dir_em = fout.mkdir("em_1")
    dir_em = fout.GetDirectory("em_1")

hist_names = ["VV", "Fake", "Top", "ZTT", "GGTT", "GGWW", "data"]

for hist_name in hist_names:
    if name == "nTrk0":
        fin = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_run2_basicsel/h0_"+hist_name+".root", "READ")
    elif name == "nTrk1":
        fin = ROOT.TFile("/eos/user/z/zohe/WWdata/ntuples_emu_run2_basicsel/h1_"+hist_name+".root", "READ")
    hist = fin.Get(hist_name+"_puWeightDown")
    
    if hist:
        dir_em.cd()
        hist_clone = hist.Clone()
        '''
        if hist_name == "data":
            hist_clone.SetName("data_obs")
        '''
        hist_clone.Write()
    else:
        print("Histogram {} not found in {}".format(hist_name, fin.GetName()))
    fin.Close()

fout.Close()
