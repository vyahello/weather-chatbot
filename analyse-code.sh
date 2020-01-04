#!/usr/bin/env bash

PACKAGE="src"


check-black() {
    printf "Start black analysis ...\n" && ( black --check ${PACKAGE} )
}


check-flake() {
    printf "Start flake8 analysis ...\n" && ( flake8 ${PACKAGE} )
}


check-unittests() {
    printf "Start unittests analysis ...\n" && pytest
}


main() {
    check-black && check-flake && check-unittests
}


main
