python ../FinalSelection_emu.py 2016pre MuonEGB exclusive data
python ../FinalSelection_emu.py 2016pre MuonEGC exclusive data
python ../FinalSelection_emu.py 2016pre MuonEGD exclusive data
python ../FinalSelection_emu.py 2016pre MuonEGE exclusive data
python ../FinalSelection_emu.py 2016pre MuonEGF exclusive data
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/data.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MuonEGB.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MuonEGC.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MuonEGD.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MuonEGE.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MuonEGF.root



python ../FinalSelection_emu.py 2016pre DYemu exclusive DY
mv /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/DYemu.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ZTT.root



python ../FinalSelection_emu.py 2016pre TTToHadronic exclusive top
python ../FinalSelection_emu.py 2016pre TTToSemiLeptonic exclusive top
python ../FinalSelection_emu.py 2016pre TTTo2L2Nu_small exclusive top
mv /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/TTTo2L2Nu.root
python ../FinalSelection_emu.py 2016pre ST_t_antitop exclusive top
python ../FinalSelection_emu.py 2016pre ST_t_top exclusive top
python ../FinalSelection_emu.py 2016pre ST_tW_antitop exclusive top
python ../FinalSelection_emu.py 2016pre ST_tW_top exclusive top
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/Top.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ST_tW_top.root



python ../FinalSelection_emu.py 2016pre WZ2Q2L exclusive VV
python ../FinalSelection_emu.py 2016pre WZ3LNu exclusive VV
python ../FinalSelection_emu.py 2016pre VV2L2Nu exclusive VV
python ../FinalSelection_emu.py 2016pre ZZ4L exclusive VV
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/VV.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/WZ3LNu.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/VV2L2Nu.root    /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/ZZ4L.root

python ../FinalSelection_emu.py 2016pre GGToWW exclusive signal
mv /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/GGToWW.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/GGWW.root
python ../FinalSelection_emu.py 2016pre GGToTauTau_Ctb20 exclusive GG
mv /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/GGToTauTau_Ctb20.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/GGTT.root

#hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/MC.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/DY.root /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/VV.root  /eos/user/z/zohe/WWdata/ntuples_emu_2016pre_basicsel/top.root

