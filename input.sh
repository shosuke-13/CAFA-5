#!/bin/bash
# Need kaggle API
COMPETITION_NAME="CAFA-5-Protein-Function-Prediction"

# Download CAFA-5 dataset
COMPETITION_PATH="input/${COMPETITION_NAME}"

kaggle competitions download -c ${COMPETITION_NAME} -p .
mkdir -p ${COMPETITION_PATH}
unzip ${COMPETITION_NAME}.zip -d ${COMPETITION_PATH}
rm ${COMPETITION_NAME}.zip
