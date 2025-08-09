# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# >>> ZSH and Oh My Zsh Setup <<<
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=(git)

source $ZSH/oh-my-zsh.sh

# >>> Custom PATH <<<
export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

# >>> Optional aliases <<<
alias update='apt update && apt upgrade -y'
alias cls='clear'

# >>> Fix for Termux Locale <<<
export LANG=en_US.UTF-8

# >>> Powerlevel10k config file auto-load (if exists) <<<
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
