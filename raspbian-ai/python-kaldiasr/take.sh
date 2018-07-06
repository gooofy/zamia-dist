#!/bin/bash

REPO=${HOME}/repo/ai/raspbian/stretch/armhf

rm -f ${REPO}/python*-kaldiasr*.deb

cp python*-kaldiasr*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

