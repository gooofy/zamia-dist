#!/bin/bash

REPO=${HOME}/repo/ai/raspbian/stretch/armhf

rm -f ${REPO}/python*-marytts*.deb

cp python*-marytts*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

