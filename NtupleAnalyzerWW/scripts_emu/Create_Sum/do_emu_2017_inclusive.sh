python ../FinalSelection_emu.py 2017 MuonEGB inclusive data
python ../FinalSelection_emu.py 2017 MuonEGC inclusive data
python ../FinalSelection_emu.py 2017 MuonEGD inclusive data
python ../FinalSelection_emu.py 2017 MuonEGE inclusive data
python ../FinalSelection_emu.py 2017 MuonEGF inclusive data
hadd -f /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/data.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/MuonEGB.root    /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/MuonEGC.root    /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/MuonEGD.root    /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/MuonEGE.root    /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/MuonEGF.root   



python ../FinalSelection_emu.py 2017 DYemu inclusive DY
mv /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/DYemu.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/DY.root


python ../FinalSelection_emu.py 2017 TTToHadronic inclusive top
python ../FinalSelection_emu.py 2017 TTToSemiLeptonic inclusive top
python ../FinalSelection_emu.py 2017 TTTo2L2Nu_small inclusive top
mv /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/TTTo2L2Nu.root
python ../FinalSelection_emu.py 2017 ST_t_antitop inclusive top
python ../FinalSelection_emu.py 2017 ST_t_top inclusive top
python ../FinalSelection_emu.py 2017 ST_tW_antitop inclusive top
python ../FinalSelection_emu.py 2017 ST_tW_top inclusive top
hadd -f /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/top.root    /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/ST_tW_top.root



python ../FinalSelection_emu.py 2017 WZ2Q2L inclusive VV
python ../FinalSelection_emu.py 2017 WZ3LNu inclusive VV
python ../FinalSelection_emu.py 2017 VV2L2Nu inclusive VV
python ../FinalSelection_emu.py 2017 ZZ4L inclusive VV
hadd -f /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/VV.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/WZ3LNu.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/VV2L2Nu.root    /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/ZZ4L.root

hadd -f /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/MC.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/DY.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/VV.root  /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2017_basicsel/top.root

