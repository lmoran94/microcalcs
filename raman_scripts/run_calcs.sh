#!/bin/bash

#python3 scripts/make_calcs_sphere.py
touch output/Raman_weight.txt
#mcrt mcrt_microcalclaser.json5
#mv output/energy_density.nc input/scale.nc
#babbage babbage_norm.json5
#cp input/scale.nc input/babbage_scaled.nc
#babbage babbage.json5
#mv output/output.csv input/weightings.csv

#for z in `seq 1 1 10`
#    do
        #echo "$z"
python3 raman_scripts/make_calcs_sphere.py

for x in `seq 0.015 0.001 0.019`

    do
        echo "$x"
        python3 raman_scripts/move_calcs.py $x
        babbage babbage_lm.json5
        mv output/output.csv weightings.csv
        python3 raman_scripts/plot_babbage.py
        python3 raman_scripts/power_change.py

                #for value in `seq 1 1 1`
                #    do

        mcrt mcrt_microcalcraman.json5
        python3 raman_scripts/spectrometer_extract.py

    done
            #done
    #done
