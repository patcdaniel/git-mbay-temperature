#!/bin/bash

# Download the CSV file
curl -o ../data/monterey-bay-aquarium-seawater-intake.csv "https://erddap.cencoos.org/erddap/tabledap/monterey-bay-aquarium-seawate.csvp?time%2Cfractional_saturation_of_oxygen_in_sea_water%2Csea_water_temperature&time%3E=2025-01-15&time%3C=2025-02-05T07%3A59%3A00Z"

echo "Download complete: mba_data.csv"