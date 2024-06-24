python hadd_HiggsCombine.py run2 data nTrk0
python hadd_HiggsCombine.py run2 VV nTrk0
python hadd_HiggsCombine.py run2 ZTT nTrk0
python hadd_HiggsCombine.py run2 Top nTrk0
python hadd_HiggsCombine.py run2 GGTT nTrk0
python hadd_HiggsCombine.py run2 GGWW nTrk0
python hadd_HiggsCombineSS.py run2 data nTrk0
python hadd_HiggsCombineSS.py run2 VV nTrk0
python hadd_HiggsCombineSS.py run2 ZTT nTrk0
python hadd_HiggsCombineSS.py run2 Top nTrk0
python create_fBkg_exclusive.py run2 nTrk0
python ../../../DataCard/Create_rootDatacard.py nTrk0 

python hadd_HiggsCombine.py run2 data nTrk1
python hadd_HiggsCombine.py run2 VV nTrk1
python hadd_HiggsCombine.py run2 ZTT nTrk1
python hadd_HiggsCombine.py run2 Top nTrk1
python hadd_HiggsCombine.py run2 GGTT nTrk1
python hadd_HiggsCombine.py run2 GGWW nTrk1
python hadd_HiggsCombineSS.py run2 data nTrk1
python hadd_HiggsCombineSS.py run2 VV nTrk1
python hadd_HiggsCombineSS.py run2 ZTT nTrk1
python hadd_HiggsCombineSS.py run2 Top nTrk1
python create_fBkg_exclusive.py run2 nTrk1 
python ../../../DataCard/Create_rootDatacard.py nTrk1