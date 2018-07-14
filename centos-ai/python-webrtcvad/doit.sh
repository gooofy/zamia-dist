#!/bin/sh

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -ba --clean python-webrtcvad.spec

