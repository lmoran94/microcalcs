#!/bin/bash

#python3 scripts/make_calcs_sphere.py
rm output/ccd_sors/*
rm output/ccd_trs/*
rm output/Raman_weight_trs.txt
rm output/Raman_weight_sors.txt
touch output/Raman_weight_trs.txt
touch output/Raman_weight_sors.txt
#mcrt mcrt_microcalclaser.json5
#mv output/energy_density.nc input/scale.nc
#babbage babbage_norm.json5
#cp input/scale.nc input/babbage_scaled.nc
#babbage babbage.json5
#mv output/output.csv input/weightings.csv
number_sors=0
number_trs=0

#for z in `seq 1 1 10`
#    do
        #echo "$z"
python3 raman_scripts/make_calcs_sphere.py

for x in `seq -0.023 0.005 0.023`

    do
        echo "$x"
        python3 raman_scripts/move_calcs.py $x
        babbage output input babbage_lm.json5
        cp output/output.csv input/weightings.csv
        python3 raman_scripts/plot_babbage.py
        python3 raman_scripts/power_change.py

                #for value in `seq 1 1 1`
                #    do

        mcrt output input mcrt_microcalcraman.json5
        python3 raman_scripts/circle_detector.py
        mv output/ccd_{sors}.nc output/ccd_sors/ccd_{sors}.nc
        mv "output/ccd_sors/ccd_{sors}.nc" "output/ccd_sors/ccd_{sors}_""$((++number_sors))"".nc"
        mv output/ccd_{trs}.nc output/ccd_trs/ccd_{trs}.nc
        mv "output/ccd_trs/ccd_{trs}.nc" "output/ccd_trs/ccd_{trs}_""$((++number_trs))"".nc"
        #python3 raman_scripts/spectrometer_extract.py

    done
            #done
    #done
