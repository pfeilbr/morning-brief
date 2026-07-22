#!/bin/bash
# Generates and publishes the daily morning brief via Claude Code (non-interactive).
# Invoked by launchd (com.pfeil.morningbrief) weekday mornings at 08:00.

set -uo pipefail

export PATH="/Users/pfeilbr/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
export HOME="/Users/pfeilbr"

REPO="/Users/pfeilbr/projects/morning-brief"
cd "$REPO" || exit 1

/Users/pfeilbr/.local/bin/claude -p "$(cat "$REPO/daily-prompt.txt")" \
  --allowedTools "Bash,Read,Write,Edit,Glob,Grep,WebSearch,WebFetch,mcp__google__*,mcp__gmail__*,mcp__google-calendar__*" \
  --max-turns 120
