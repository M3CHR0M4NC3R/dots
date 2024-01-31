#
# ~/.bashrc
#

# If not running interactively, don't do anything

#this is the variable for my terminal in sxhkd

[[ $- != *i* ]] && return
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias pcm='sudo pacman -S'
alias neofetch='fastfetch'
alias vi='vim'
PS1='[\u@\h \W]\$ '
export PATH="$HOME/.config/scripts:$PATH"
#if [[ `ps ho command $(ps ho ppid $$)` == 'urxvt' ]]; then
#	clear
#fi
#pokemon-colorscripts -r 1-3
(cat $HOME/.config/wpg/sequences &)
