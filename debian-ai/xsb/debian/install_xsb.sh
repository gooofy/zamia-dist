#!/bin/bash

mkdir -p debian/xsb-doc/usr/share/doc/xsb-doc
cp FAQ LICENSE README debian/xsb-doc/usr/share/doc/xsb-doc

mkdir -p debian/xsb/opt/xsb
cp -rp * debian/xsb/opt/xsb
rm debian/xsb/opt/xsb/FAQ
rm debian/xsb/opt/xsb/LICENSE
rm debian/xsb/opt/xsb/README

DEB_BUILD_ROOT=`pwd`

sed -i "s^$DEB_BUILD_ROOT^^g" debian/xsb/opt/xsb/config/*/emuMakefile
sed -i "s^$DEB_BUILD_ROOT^^g" debian/xsb/opt/xsb/config/*/topMakefile
sed -i "s^$DEB_BUILD_ROOT^^g" debian/xsb/opt/xsb/config/*/lib/xsb_configuration.P

mkdir -p debian/xsb/usr/bin
cp debian/xsb.bin debian/xsb/usr/bin/xsb

mkdir -p debian/xsb/usr/lib
mv debian/xsb/opt/xsb/emu/libxsb.so debian/xsb/usr/lib
rm debian/xsb/opt/xsb/config/*/bin/libxsb.so

mkdir -p debian/xsb/usr/share/man/man1
mv debian/xsb/opt/xsb/docs/userman/xsb.1 debian/xsb/usr/share/man/man1

