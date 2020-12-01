printf '~~~ ADVENT OF CODE 2020 SOLUTIONS ~~~\n'
printf '             .-"```"-.\n'
printf '            /_\ _ _ __\\\n'
printf '           | /{` ` `  `}\n'
printf '           {} {_,_,_,_,}\n'
printf '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'

dayNumber=1
for day in `ls -d */ | egrep '^day[0-9]+'`
do
    printf "Day $dayNumber\n"
    part=1
    for script in `ls $day | egrep '^part[0-9]+\.py'`
    do
        answer=`python3 $day$script`
        printf "\\tAnswer for part $part: $answer\n"
        part=$(( part + 1 ))
    done
    dayNumber=$(( dayNumber + 1 ))
done
