#!/bin/bash

cd opt/kaldi/src/lib 

for i in *.so ; do 
    NEWLNK=`readlink $i | sed 's/\/home\/bofh\/build\/raspbian-ai\/libkaldi-asr\/libkaldi-asr-.......\/src/../g'` 
    echo $NEWLNK 
    rm $i
    ln -s $NEWLNK $i
done

