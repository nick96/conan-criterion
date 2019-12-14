#!/bin/bash

set -e
set -x

if [[ "TRAVIS_OS_NAME" == "windows" ]]
then
    choco install python --version 3.8
    export PATH="/c/Python38:/c/Python38/Scripts:$PATH"
    pip3 install conan
    pip3 install conan_package_tools bincrafters_package_tools
else
    pip install conan --upgrade
    pip install conan_package_tools bincrafters_package_tools
fi


conan user
