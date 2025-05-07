#!/bin/bash

CHEAT_DIR="./cheats"

GREEN=$(tput setaf 2)
RED=$(tput setaf 1)
CYAN=$(tput setaf 6)
RESET=$(tput sgr0)

function banner() {
  echo "${CYAN}=== Linux Cheat Sheet CLI Tool ===${RESET}"
}

function usage() {
  banner
  echo -e "Usage:"
  echo -e "  ${GREEN}./linuxcheat.sh list${RESET}                  - Show all available categories"
  echo -e "  ${GREEN}./linuxcheat.sh show <category>${RESET}      - Show cheat sheet for a category"
  echo -e "  ${GREEN}./linuxcheat.sh search <keyword>${RESET}     - Search all cheat sheets for a command or keyword"
}

function show_categories() {
  echo "${CYAN}Available Categories:${RESET}"
  for file in "$CHEAT_DIR"/*.txt; do
    basename "$file" .txt
  done
}

function show_cheats() {
  local category=$1
  local file="$CHEAT_DIR/$category.txt"
  if [[ -f "$file" ]]; then
    echo "${CYAN}Showing cheat sheet for: $category${RESET}"
    cat "$file"
  else
    echo "${RED}Error:${RESET} Category '${category}' not found."
  fi
}

function search_cheats() {
  local keyword=$1
  echo "${CYAN}Searching for '${keyword}'...${RESET}"
  grep -rin --color=always "$keyword" "$CHEAT_DIR"/*.txt || echo "${RED}No results found.${RESET}"
}

# Main command handler
case "$1" in
  list)
    show_categories
    ;;
  show)
    if [ -z "$2" ]; then usage; else show_cheats "$2"; fi
    ;;
  search)
    if [ -z "$2" ]; then usage; else search_cheats "$2"; fi
    ;;
  *)
    usage
    ;;
esac