next_day=`ls | grep '^day' | wc -l`
dir=day$(( $next_day + 1 ))
mkdir $dir ; touch $dir/input.txt $dir/part1.py $dir/part2.py
