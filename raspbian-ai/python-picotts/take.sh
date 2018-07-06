#!/bin/bash

REPO=${HOME}/repo/ai/raspbian/stretch/armhf

rm -f ${REPO}/python*-picotts*.deb

cp python*-picotts*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

