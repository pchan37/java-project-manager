#!/bin/bash -e

bin_line='PATH=$HOME/.local/java-project-manager/bin:$PATH'
activation_line='source $HOME/.config/java-project-manager/java-project-manager.sh'
if [ -f $HOME/.zshrc ]; then
    echo "Installing..."
    grep -q -F $bin_line $HOME/.zshrc || echo -n "$bin_line\n" >> $HOME/.zshrc
    grep -q -F $activation_line $HOME/.zshrc || echo -n "$activation_line\n" >> $HOME/.zshrc
    mkdir -p $HOME/.local/java-project-manager/bin
    mkdir -p $HOME/.config/java-project-manager
    cp SkeletonGenerator.py $HOME/.local/java-project-manager/bin
    cp ProjectTester.py $HOME/.local/java-project-manager/bin
    cp ProjectManagerInterface.py $HOME/.local/java-project-manager/bin
    cp java-project-manager.sh $HOME/.config/java-project-manager/java-project-manager.sh
    source $HOME/.config/java-project-manager/java-project-manager.sh
    echo "Done!"
else
    if [ -f $HOME/.bashrc ]; then
        echo "Installing..."
        grep -q -F $bin_line $HOME/.bashrc || echo -n $bin_line >> $HOME/.bashrc
        grep -q -F $activation_line $HOME/.bashrc || echo -n $activation_line >> $HOME/.bashrc
        mkdir -p $HOME/.local/java-project-manager/bin
        mkdir -p $HOME/.config/java-project-manager
        cp SkeletonGenerator.py $HOME/.local/java-project-manager/bin
        cp ProjectTester.py $HOME/.local/java-project-manager/bin
        cp ProjectManagerInterface.py $HOME/.local/java-project-manager/bin
        cp java-project-manager.sh $HOME/.config/java-project-manager/java-project-manager.sh
        source $HOME/.config/java-project-manager/java-project-manager.sh
        echo "Done!"
    else
        echo "System not supported at this time..."
    fi
fi
