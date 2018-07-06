#!/bin/bash

REPO=${HOME}/repo/ai/debian/stretch/amd64

rm -f ${REPO}/python*-nltools*.deb

cp python*-nltools*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

