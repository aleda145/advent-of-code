#!/bin/bash

set -euxo pipefail

year=${1:-$(date +%Y)}
day=${2:-$(date +%d)}

echo "Creating files for $year-$day"

dir="./${year}/${day}"

mkdir -p "${dir}"

pythonfile="${dir}/${day}.py"
if [ ! -f "$pythonfile" ]
then
    {
    echo 'import util'
    echo 'inp = util.input_as_lines("input")'
    echo 'sample = util.input_as_lines("sample_input")'
    } >> "$pythonfile"
fi

sample_input="${dir}/sample_input"
test -f "$sample_input" || touch "$sample_input"

input="${dir}/input"

aoc_day=$((10#$day)) # Remove padded 0, which I like, but advent of code does not like
if [ ! -f "$input" ]
then
    curl -s -S -f -o "$input" \
    -H "cookie: session=${AOC_SESSION_COOKIE}" \
    -w "%{http_code}\n" \
    "https://adventofcode.com/$year/day/$aoc_day/input"
fi
