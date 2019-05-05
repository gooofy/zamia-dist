#!/bin/bash

REPO=${HOME}/repo/ai/raspbian/stretch/armhf/

rm -f ${REPO}/libkaldi-asr*.deb

rm libkaldi-asr-dbgsym_*.deb
cp libkaldi-asr*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

