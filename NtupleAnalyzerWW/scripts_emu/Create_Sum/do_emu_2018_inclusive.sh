#python ../FinalSelection_emu.py 2018 MuonEGA inclusive data
#python ../FinalSelection_emu.py 2018 MuonEGB inclusive data
#python ../FinalSelection_emu.py 2018 MuonEGC inclusive data
#python ../FinalSelection_emu.py 2018 MuonEGD inclusive data
#hadd -f /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/data.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/MuonEGA.root    /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/MuonEGB.root    /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/MuonEGC.root    /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/MuonEGD.root



#python ../FinalSelection_emu.py 2018 DYemu inclusive DY
#mv /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/DYemu.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/DY.root



#python ../FinalSelection_emu.py 2018 TTToHadronic inclusive top
#python ../FinalSelection_emu.py 2018 TTToSemiLeptonic inclusive top
#python ../FinalSelection_emu.py 2018 TTTo2L2Nu_small inclusive top
#mv /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/TTTo2L2Nu.root
#python ../FinalSelection_emu.py 2018 ST_t_antitop inclusive top
#python ../FinalSelection_emu.py 2018 ST_t_top inclusive top
#python ../FinalSelection_emu.py 2018 ST_tW_antitop inclusive top
#python ../FinalSelection_emu.py 2018 ST_tW_top inclusive top
#hadd -f /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/top.root    /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/ST_tW_top.root



python ../FinalSelection_emu.py 2018 WZ2Q2L inclusive VV
python ../FinalSelection_emu.py 2018 WZ3LNu inclusive VV
python ../FinalSelection_emu.py 2018 VV2L2Nu_0 inclusive VV
mv /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/VV2L2Nu_0.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/VV2L2Nu.root
python ../FinalSelection_emu.py 2018 ZZ4L inclusive VV
hadd -f /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/VV.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/WZ3LNu.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/VV2L2Nu.root    /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/ZZ4L.root

hadd -f /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/MC.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/DY.root /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/VV.root  /eos/user/z/zohe/WWdata/inclusive/ntuples_emu_2018_basicsel/top.root

