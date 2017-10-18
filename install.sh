#!/bin/bash -e

if [ -f $HOME/.zshrc ]; then
    echo "source $HOME/.java-project-manager.sh" >> $HOME/.zshrc
    mkdir -p $HOME/bin
    mv SkeletonGenerator.py $HOME/bin
    mv SkeletonGeneratorInterface.py $HOME/bin
    mv java-project-manager.sh $HOME/.java-project-manager.sh
    source $HOME/.java-project-manager.sh
else
    if [ -f $HOME/.bashrc ]; then
        echo "source $HOME/.java-project-manager.sh" >> $HOME/.bashrc
        mkdir -p $HOME/bin
        mv SkeletonGenerator.py $HOME/bin
        mv SkeletonGeneratorInterface.py $HOME/bin
        mv java-project-manager.sh $HOME/.java-project-manager.sh
        source $HOME/.java-project-manager.sh
    fi
fi
