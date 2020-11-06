#!/bin/sh

for c in A B C D E F; do
    mkdir challenge$c
    cat > challenge$c/README.md <<EOF
# Challenge $c
EOF
done
