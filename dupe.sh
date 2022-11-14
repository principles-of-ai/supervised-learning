#!/bin/sh

for file in *.png; do
    NAME=$(openssl rand -hex 10)
    #cp "$file" "${file%.png}$NAME.png" # Don't duplicate file name just rename it
    cp "$file" "$NAME.png"
    echo "Copying $file as $NAME"
done