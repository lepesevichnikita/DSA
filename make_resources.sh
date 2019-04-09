#!/bin/sh
rm -rf ./resources_rc.py && pyrcc5 ./resources.qrc -o ./resources_rc.py
