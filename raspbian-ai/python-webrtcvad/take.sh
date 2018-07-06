#!/bin/bash

REPO=${HOME}/repo/ai/raspbian/stretch/armhf

rm -f ${REPO}/python*-webrtcvad*.deb

cp python*-webrtcvad*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

