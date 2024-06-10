python ../FinalSelection_emu.py 2016pre MuonEGB FR data
python ../FinalSelection_emu.py 2016pre MuonEGC FR data
python ../FinalSelection_emu.py 2016pre MuonEGD FR data
python ../FinalSelection_emu.py 2016pre MuonEGE FR data
python ../FinalSelection_emu.py 2016pre MuonEGF FR data
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/data.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/MuonEGB.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/MuonEGC.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/MuonEGD.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/MuonEGE.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/MuonEGF.root



python ../FinalSelection_emu.py 2016pre DYemu FR DY
mv /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/DYemu.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/DY.root


python ../FinalSelection_emu.py 2016pre TTToHadronic FR top
python ../FinalSelection_emu.py 2016pre TTToSemiLeptonic FR top
python ../FinalSelection_emu.py 2016pre TTTo2L2Nu_small FR top
mv /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/TTTo2L2Nu.root
python ../FinalSelection_emu.py 2016pre ST_t_antitop FR top
python ../FinalSelection_emu.py 2016pre ST_t_top FR top
python ../FinalSelection_emu.py 2016pre ST_tW_antitop FR top
python ../FinalSelection_emu.py 2016pre ST_tW_top FR top
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/top.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/ST_tW_top.root



python ../FinalSelection_emu.py 2016pre WZ2Q2L FR VV
python ../FinalSelection_emu.py 2016pre WZ3LNu FR VV
python ../FinalSelection_emu.py 2016pre VV2L2Nu FR VV
python ../FinalSelection_emu.py 2016pre ZZ4L FR VV
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/VV.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/WZ3LNu.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/VV2L2Nu.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/ZZ4L.root

hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/MC.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/DY.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/VV.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016pre_basicsel/top.root

python ../Compute_FR_emu.py 2016pre 
python ../Compute_FRnTrk_emu.py 2016pre