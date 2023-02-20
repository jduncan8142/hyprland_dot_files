#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias ll='ls -lash --color=auto'

alias paru='yay'

PS1='[\u@\h \W]\$ '
neofetch
