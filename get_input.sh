input_day=$1
cookies=`cat .cookies`
pattern="^[0-9]+$"
iterator=""
if ! [[ -z "$1" ]] && [[ $1 =~ $pattern ]]
then
    iterator=$1
else
    iterator=`ls -d */ | egrep -oh '[0-9]+' | sed -e 's/^0//g'`
fi

for day in $iterator
do
    dirNum=`printf "%02d" $day`
    mkdir -p day$dirNum
    printf "Getting input for day $day...\n"
    printf '%s' "`curl -H "cookie: $cookies" https://adventofcode.com/2020/day/$day/input`" > day$dirNum/input.txt
done
