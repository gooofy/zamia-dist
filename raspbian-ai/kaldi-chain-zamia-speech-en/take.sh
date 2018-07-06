#!/bin/bash

REPO=${HOME}/repo/ai/raspbian/stretch/armhf
PACKAGE=kaldi-chain-zamia-speech-en

rm -f ${REPO}/${PACKAGE}*.deb

cp ${PACKAGE}*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

