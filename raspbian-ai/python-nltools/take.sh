#!/bin/bash

REPO=${HOME}/repo/ai/raspbian/stretch/armhf

rm -f ${REPO}/python*-nltools*.deb

cp python*-nltools*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

