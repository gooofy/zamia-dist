#!/bin/bash

REPO=${HOME}/repo/ai/debian/stretch/amd64

rm -f ${REPO}/python*-num2words*.deb

cp python*-num2words*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

