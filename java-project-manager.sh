#!/bin/bash -e

create() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/.local/java-project-manager/bin/ProjectManagerInterface.py 'create' $PWD
}

add() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/.local/java-project-manager/bin/ProjectManagerInterface.py 'add' $PWD $1
}

generate() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/.local/java-project-manager/bin/ProjectManagerInterface.py 'generate' $PWD
}

clean() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/.local/java-project-manager/bin/ProjectManagerInterface.py 'clean' $PWD
}

compile (){
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/.local/java-project-manager/bin/ProjectManagerInterface.py 'compile' $PWD
}

run() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/.local/java-project-manager/bin/ProjectManagerInterface.py 'run' $PWD
}

javatest() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    python $HOME/.local/java-project-manager/bin/ProjectManagerInterface.py 'javatest' $PWD
}
