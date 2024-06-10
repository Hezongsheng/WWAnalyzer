python ../FinalSelection_emu.py 2016post MuonEGF FR data
python ../FinalSelection_emu.py 2016post MuonEGG FR data
python ../FinalSelection_emu.py 2016post MuonEGH FR data
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/data.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/MuonEGF.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/MuonEGG.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/MuonEGH.root 



python ../FinalSelection_emu.py 2016post DYemu FR DY
mv /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/DYemu.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/DY.root


python ../FinalSelection_emu.py 2016post TTToHadronic FR top
python ../FinalSelection_emu.py 2016post TTToSemiLeptonic FR top
python ../FinalSelection_emu.py 2016post TTTo2L2Nu_small FR top
mv /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/TTTo2L2Nu_small.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/TTTo2L2Nu.root
python ../FinalSelection_emu.py 2016post ST_t_antitop FR top
python ../FinalSelection_emu.py 2016post ST_t_top FR top
python ../FinalSelection_emu.py 2016post ST_tW_antitop FR top
python ../FinalSelection_emu.py 2016post ST_tW_top FR top
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/top.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/TTToHadronic.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/TTToSemiLeptonic.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/TTTo2L2Nu.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/ST_t_antitop.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/ST_t_top.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/ST_tW_antitop.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/ST_tW_top.root



python ../FinalSelection_emu.py 2016post WZ2Q2L FR VV
python ../FinalSelection_emu.py 2016post WZ3LNu FR VV
python ../FinalSelection_emu.py 2016post VV2L2Nu FR VV
python ../FinalSelection_emu.py 2016post ZZ4L FR VV
hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/VV.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/WZ2Q2L.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/WZ3LNu.root    /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/VV2L2Nu.root   /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/ZZ4L.root

hadd -f /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/MC.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/DY.root /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/VV.root  /eos/user/z/zohe/WWdata/FR/ntuples_emu_2016post_basicsel/top.root

python ../Compute_FR_emu.py 2016post 
#python ../Compute_FRnTrk_emu.py 2016post