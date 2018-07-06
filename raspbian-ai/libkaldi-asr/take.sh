#!/bin/bash

REPO=${HOME}/repo/ai/raspbian/stretch/armhf

rm -f ${REPO}/libkaldi-asr*.deb

cp libkaldi-asr*.deb ${REPO}

pushd ${REPO}
rm Packages.gz
dpkg-scanpackages . /dev/null | gzip -9c > Packages.gz
./update.sh
popd

