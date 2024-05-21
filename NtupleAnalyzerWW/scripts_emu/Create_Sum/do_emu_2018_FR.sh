python ../FinalSelection_emu.py 2018 MuonEGA FR data
python ../FinalSelection_emu.py 2018 MuonEGB FR data
python ../FinalSelection_emu.py 2018 MuonEGC FR data
python ../FinalSelection_emu.py 2018 MuonEGD FR data
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/data.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/MuonEGA.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/MuonEGB.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/MuonEGC.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/MuonEGD.root



python ../FinalSelection_emu.py 2018 DYemu FR DY
mv /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/DYemu.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/DY.root



python ../FinalSelection_emu.py 2018 TTToHadronic FR top
python ../FinalSelection_emu.py 2018 TTToSemiLeptonic FR top
python ../FinalSelection_emu.py 2018 TTTo2L2Nu_small FR top
mv /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/TTTo2L2Nu.root
python ../FinalSelection_emu.py 2018 ST_t_antitop FR top
python ../FinalSelection_emu.py 2018 ST_t_top FR top
python ../FinalSelection_emu.py 2018 ST_tW_antitop FR top
python ../FinalSelection_emu.py 2018 ST_tW_top FR top
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/top.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/ST_tW_top.root



python ../FinalSelection_emu.py 2018 WZ2Q2L FR VV
python ../FinalSelection_emu.py 2018 WZ3LNu FR VV
python ../FinalSelection_emu.py 2018 VV2L2Nu_0 FR VV
mv /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/VV2L2Nu_0.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/VV2L2Nu.root
python ../FinalSelection_emu.py 2018 ZZ4L FR VV
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/VV.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/WZ3LNu.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/VV2L2Nu.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/ZZ4L.root

hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/MC.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/DY.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/VV.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2018_basicsel/top.root

python ../Compute_FR_emu.py 2018
python ../Compute_FRnTrk_emu.py 2018