#!/bin/bash

REPO=${HOME}/repo/ai/raspbian/stretch/armhf

rm -f ${REPO}/python*-espeakng*.deb

cp python*-espeakng*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

