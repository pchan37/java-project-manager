#!/bin/bash -e

create() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/bin/SkeletonGeneratorInterface.py 'create' $PWD
}

add() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/bin/SkeletonGeneratorInterface.py 'add' $PWD $1
}

generate() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/bin/SkeletonGeneratorInterface.py 'generate' $PWD
}

clean() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/bin/SkeletonGeneratorInterface.py 'clean' $PWD
}

run() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/bin/SkeletonGeneratorInterface.py 'run' $PWD
}
