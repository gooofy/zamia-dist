#!/bin/bash

REPO=${HOME}/repo/ai/debian/stretch/amd64/

rm -f ${REPO}/python*-picotts*.deb

cp python*-picotts*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

