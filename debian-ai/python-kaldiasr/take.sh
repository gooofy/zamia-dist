#!/bin/bash

REPO=${HOME}/repo/ai/debian/stretch/amd64/

rm -f ${REPO}/python*-kaldiasr*.deb

cp python*-kaldiasr*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

