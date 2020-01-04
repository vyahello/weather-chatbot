#!/usr/bin/env bash

PACKAGE="src"


check-black() {
    printf "Start black analysis ..." && ( black --check ${PACKAGE} )
}


check-flake() {
    printf "Start flake8 analysis ..." && ( flake8 ${PACKAGE} )
}


check-unittests() {
    printf "Start unittests analysis ..." && pytest
}


main() {
    check-black && check-flake && check-unittests
}


main