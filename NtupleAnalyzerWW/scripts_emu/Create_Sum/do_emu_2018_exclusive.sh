python ../FinalSelection_emu.py 2018 MuonEGA exclusive data
python ../FinalSelection_emu.py 2018 MuonEGB exclusive data
python ../FinalSelection_emu.py 2018 MuonEGC exclusive data
python ../FinalSelection_emu.py 2018 MuonEGD exclusive data
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/data.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/MuonEGA.root    /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/MuonEGB.root    /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/MuonEGC.root    /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/MuonEGD.root



python ../FinalSelection_emu.py 2018 DYemu exclusive DY
mv /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/DYemu.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/DY.root



python ../FinalSelection_emu.py 2018 TTToHadronic exclusive top
python ../FinalSelection_emu.py 2018 TTToSemiLeptonic exclusive top
python ../FinalSelection_emu.py 2018 TTTo2L2Nu_small exclusive top
mv /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/TTTo2L2Nu.root
python ../FinalSelection_emu.py 2018 ST_t_antitop exclusive top
python ../FinalSelection_emu.py 2018 ST_t_top exclusive top
python ../FinalSelection_emu.py 2018 ST_tW_antitop exclusive top
python ../FinalSelection_emu.py 2018 ST_tW_top exclusive top
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/top.root    /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ST_tW_top.root



python ../FinalSelection_emu.py 2018 WZ2Q2L exclusive VV
python ../FinalSelection_emu.py 2018 WZ3LNu exclusive VV
python ../FinalSelection_emu.py 2018 VV2L2Nu_0 exclusive VV
mv /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/VV2L2Nu_0.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/VV2L2Nu.root
python ../FinalSelection_emu.py 2018 ZZ4L exclusive VV
hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/VV.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/WZ3LNu.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/VV2L2Nu.root    /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/ZZ4L.root

python ../FinalSelection_emu.py 2018 GGToWW exclusive signal
python ../FinalSelection_emu.py 2018 GGToTauTau_Ctb20 exclusive GG
mv /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/GGToTauTau_Ctb20.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/GGToTauTau.root

#hadd -f /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/MC.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/DY.root /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/VV.root  /eos/user/z/zohe/WWdata/ntuples_emu_2018_basicsel/top.root

