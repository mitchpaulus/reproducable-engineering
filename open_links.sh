#!/usr/bin/fish

for url in (grep -o '(.*)' README.md )
    "/mnt/c/Program Files/Firefox Developer Edition/firefox.exe"  (string sub -s 2 -l (math (string length "$url") - 2) "$url");
end

# Start up IDFEditor
/mnt/c/EnergyPlusV9-4-0/PreProcess/IDFEditor/IDFEditor.exe &

# Start up EPPlus Run
/mnt/c/EnergyPlusV9-4-0/EP-Launch.exe &
