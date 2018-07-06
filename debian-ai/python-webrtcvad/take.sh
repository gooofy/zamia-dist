#!/bin/bash

REPO=${HOME}/repo/ai/debian/stretch/amd64/

rm -f ${REPO}/python*-webrtcvad*.deb

cp python*-webrtcvad*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

