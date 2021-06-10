#!/bin/bash

#python3 scripts/make_calcs_sphere.py
touch output/Raman_weight_trs.txt
touch output/Raman_weight_sors.txt
#mcrt mcrt_microcalclaser.json5
#mv output/energy_density.nc input/scale.nc
#babbage babbage_norm.json5
#cp input/scale.nc input/babbage_scaled.nc
#babbage babbage.json5
#mv output/output.csv input/weightings.csv
number_sors_opt=0
number_trs_opt=0

#for z in `seq 1 1 10`
#    do
        #echo "$z"
python3 raman_scripts/make_calcs_sphere.py

for x in `seq -0.023 0.001 0.023`
    do
        ((number_sors_opt++))
        ((number_trs_opt++))
        number_sors_perp=0
        number_trs_perp=0
        for y in `seq -0.038 0.002 0.038`
            do
                echo "$x"
                echo "$y"
                python3 raman_scripts/move_calcs_map.py $x $y
                babbage output input babbage_lm.json5
                cp output/output.csv input/weightings.csv
                python3 raman_scripts/plot_babbage.py
                python3 raman_scripts/power_change.py

                mcrt output input mcrt_microcalcraman.json5
                #python3 raman_scripts/circle_detector.py
                mv output/ccd_{sors}.nc output/ccd_sors_map/ccd_{sors}.nc
                mv "output/ccd_sors_map/ccd_{sors}.nc" "output/ccd_sors_map/ccd_{sors}_""$((number_sors_opt))""_""$((++number_sors_perp))"".nc"
                mv output/ccd_{trs}.nc output/ccd_trs_map/ccd_{trs}.nc
                mv "output/ccd_trs_map/ccd_{trs}.nc" "output/ccd_trs_map/ccd_{trs}_""$((number_trs_opt))""_""$((++number_trs_perp))"".nc"
                #python3 raman_scripts/spectrometer_extract.py

            done
    done
