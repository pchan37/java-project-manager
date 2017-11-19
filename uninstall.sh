#!/bin/bash

bin_line='PATH=$HOME/.local/java-project-manager/bin:$PATH'
activation_line='source $HOME/.config/java-project-manager/java-project-manager.sh'

echo -n "Are you sure you want to uninstall java-project-manager? [Y/N] "
read user_input

case $user_input in
    [yY])
        echo ""
        echo "Uninstalling..."
        rm -rf $HOME/.local/java-project-manager/
        rm -rf $HOME/.config/java-project-manager/
        if [ -f $HOME/.zshrc ] && grep -q -F $bin_line $HOME/.zshrc; then
            safe_pattern=$(printf '%s\n' "$bin_line" | sed 's/[[\.*^$/]/\\&/g')
            sed -i "/$safe_pattern/d" $HOME/.zshrc
            safe_pattern=$(printf '%s\n' "$activation_line" | sed 's/[[\.*^$/]/\\&/g')
            sed -i "/$safe_pattern/d" $HOME/.zshrc
        fi
        if [ -f $HOME/.bashrc ] && grep -q -F $bin_line $HOME/.bashrc; then
            safe_pattern=$(printf '%s\n' "$bin_line" | sed 's/[[\.*^$/]/\\&/g')
            sed -i "/$safe_pattern/d" $HOME/.bashrc
            safe_pattern=$(printf '%s\n' "$activation_line" | sed 's/[[\.*^$/]/\\&/g')
            sed -i "/$safe_pattern/d" $HOME/.bashrc
        fi
        echo "Done!  You will need to close the current terminal and open a new one for the changes to take effect."
        ;;
    *)
        echo "Exiting..."
        ;;
esac
