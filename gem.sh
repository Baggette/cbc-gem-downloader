#!/bin/bash
if ! command -v yt-dlp; then
    echo "yt-dlp not installed"  
    echo "please install yt-dlp"
else
    echo "Please enter the browser to provide cookies from (optionally add the profile using <browser>:<profile>, you also need to be signed into cbc gem within the specified browser)..."
    read browser
    echo "Please enter your email for cbc gem..."
    read email
    echo "Please enter your password..."
    read password
    echo "Please enter the link on cbc to download from..."
    read link
    yt-dlp -F --cookies-from-browser $browser --username $email --password $password $link
    echo "Please provide a dir to download to..."
    read dir
    echo "Please select a resolution and audio to download (eg: hls-1234+hls-audio-English)"
    read format
    echo "If you have any more command args for yt-dlp please specify them now. (eg --no-overwrites)"
    read cmds
    yt-dlp -f $format -P $dir --cookies-from-browser $browser --username $email --password $password $cmds $link
    echo "Done!"
fi
