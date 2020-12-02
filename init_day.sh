next_day=`ls -d */ | egrep '^day[0-9]+/$' | wc -l`
dir=day$(( $next_day + 1 ))
mkdir $dir ; touch $dir/input.txt $dir/part1.py $dir/part2.py
