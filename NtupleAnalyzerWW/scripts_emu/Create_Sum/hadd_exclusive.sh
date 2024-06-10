#2016pre    data
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/data.root     /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MuonEGB.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MuonEGC.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MuonEGD.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MuonEGE.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MuonEGF.root

#2016pre    DY
mv /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/DYemu.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ZTT.root

#2016pre  top
mv /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/TTTo2L2Nu.root
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/Top.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ST_tW_top.root

#2016pre  VV
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/VV.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/WZ3LNu.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/VV2L2Nu.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ZZ4L.root

#2016pre  MC
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MC.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ZTT.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/VV.root  /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/Top.root

#2016pre GGTT
mv  /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/GGToTauTau_Ctb20.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/GGTT.root

#2016pre GGWW
mv /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/GGToWW.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/GGWW.root



#2016post   data
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/data.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/MuonEGF.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/MuonEGG.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/MuonEGH.root 

#2016post   DY
mv /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/DYemu.root /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/ZTT.root

#2016post  top
mv /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/TTTo2L2Nu.root
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/Top.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/ST_tW_top.root

#2016post  VV
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/VV.root /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/WZ3LNu.root /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/VV2L2Nu.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/ZZ4L.root

#2016post  MC
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/MC.root /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/ZTT.root /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/VV.root  /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/Top.root

#2016pre GGTT
mv  /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/GGToTauTau_Ctb20.root /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/GGTT.root

#2016pre GGWW
mv /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/GGToWW.root /eos/user/z/zohe/WWdata/ntuples_emu_2016post_basicsel/GGWW.root

#2017   data
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/data.root /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/MuonEGB.root    /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/MuonEGC.root    /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/MuonEGD.root    /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/MuonEGE.root    /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/MuonEGF.root

#2017   DY
mv /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/DYemu.root /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/ZTT.root

#2017  top
mv /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/TTTo2L2Nu.root
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/Top.root    /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/ST_tW_top.root

#2017  VV
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/VV.root /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/WZ3LNu.root /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/VV2L2Nu.root    /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/ZZ4L.root

#2017  MC
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/MC.root /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/ZTT.root /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/VV.root  /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/Top.root

#2017 GGTT
mv  /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/GGToTauTau_Ctb20.root /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/GGTT.root

#2017 GGWW
mv /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/GGToWW.root /eos/user/z/zohe/WWdata/ntuples_emu_2017_basicsel/GGWW.root

#2018   data
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/data.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/MuonEGA.root    /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/MuonEGB.root    /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/MuonEGC.root    /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/MuonEGD.root

#2018   DY
mv /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/DYemu.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ZTT.root

#2018  top
mv /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/TTTo2L2Nu.root
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/Top.root    /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ST_tW_top.root

#2018  VV
mv /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/VV2L2Nu_0.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/VV2L2Nu.root
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/VV.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/WZ3LNu.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/VV2L2Nu.root    /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ZZ4L.root

#2018  MC
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/MC.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ZTT.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/VV.root  /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/Top.root

#2018 GGTT
mv  /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/GGToTauTau_Ctb20.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/GGTT.root

#2018 GGWW
mv /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/GGToWW.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/GGWW.root