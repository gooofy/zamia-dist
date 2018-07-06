#!/bin/bash

REPO=${HOME}/repo/ai/raspbian/stretch/armhf

rm -f ${REPO}/python*-num2words*.deb

cp python*-num2words*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

