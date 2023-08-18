#!/bin/bash
set -ex


cd NeuroML2/nmllite
./clean.sh 
python CreateNetwork.py
cd -

omv all -V

echo
echo "** All generated and tested! **"


