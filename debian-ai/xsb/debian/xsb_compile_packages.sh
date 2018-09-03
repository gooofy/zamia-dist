#!/bin/bash

pushd packages
for i in *.P ; do
    if [ -e ${i} ] ; then
        ../bin/xsb -e "compile('${i}')." < /dev/null
    fi
done
popd

for M in packages/* ; do

    if [ -d ${M} ] ; then

        pushd $M

        for i in *.P ; do
            if [ -e ${i} ] ; then
                ../../bin/xsb -e "compile('${i}')." < /dev/null
            fi
        done

        popd
    fi
done

