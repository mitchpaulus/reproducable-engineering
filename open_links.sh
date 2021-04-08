#!/usr/bin/fish

for url in (grep -o '(.*)' README.md ); "/mnt/c/Program Files/Firefox Developer Edition/firefox.exe"  (string sub -s 2 -l (math (string length "$url") - 2) "$url"); end
