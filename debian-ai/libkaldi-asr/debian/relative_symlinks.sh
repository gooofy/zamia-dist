#!/bin/bash

for SYMLINK in *.so ; do

	OLD_SYMLINK_TARGET=`readlink ${SYMLINK}`
	MY_PWD=`pwd`

	NEW_SYMLINK_TARGET=`realpath --relative-to ${MY_PWD} ${OLD_SYMLINK_TARGET}`

	echo rm "${SYMLINK}"
	rm "${SYMLINK}"
	echo ln -s "${NEW_SYMLINK_TARGET}" "${SYMLINK}"
	ln -s "${NEW_SYMLINK_TARGET}" "${SYMLINK}"

done



