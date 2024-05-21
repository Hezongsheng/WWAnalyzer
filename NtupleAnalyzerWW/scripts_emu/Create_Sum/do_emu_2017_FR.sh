python ../FinalSelection_emu.py 2017 MuonEGB FR data
python ../FinalSelection_emu.py 2017 MuonEGC FR data
python ../FinalSelection_emu.py 2017 MuonEGD FR data
python ../FinalSelection_emu.py 2017 MuonEGE FR data
python ../FinalSelection_emu.py 2017 MuonEGF FR data
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/data.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/MuonEGB.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/MuonEGC.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/MuonEGD.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/MuonEGE.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/MuonEGF.root



python ../FinalSelection_emu.py 2017 DYemu FR DY
mv /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/DYemu.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/DY.root


python ../FinalSelection_emu.py 2017 TTToHadronic FR top
python ../FinalSelection_emu.py 2017 TTToSemiLeptonic FR top
python ../FinalSelection_emu.py 2017 TTTo2L2Nu_small FR top
mv /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/TTTo2L2Nu.root
python ../FinalSelection_emu.py 2017 ST_t_antitop FR top
python ../FinalSelection_emu.py 2017 ST_t_top FR top
python ../FinalSelection_emu.py 2017 ST_tW_antitop FR top
python ../FinalSelection_emu.py 2017 ST_tW_top FR top
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/top.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/ST_tW_top.root



python ../FinalSelection_emu.py 2017 WZ2Q2L FR VV
python ../FinalSelection_emu.py 2017 WZ3LNu FR VV
python ../FinalSelection_emu.py 2017 VV2L2Nu FR VV
python ../FinalSelection_emu.py 2017 ZZ4L FR VV
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/VV.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/WZ3LNu.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/VV2L2Nu.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/ZZ4L.root

hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/MC.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/DY.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/VV.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2017_basicsel/top.root

python ../Compute_FR_emu.py 2017 
python ../Compute_FRnTrk_emu.py 2017