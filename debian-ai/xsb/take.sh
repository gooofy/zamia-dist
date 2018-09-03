#!/bin/bash

REPO=${HOME}/repo/ai/debian/stretch/amd64/

rm -f ${REPO}/xsb*.deb

cp xsb*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

