day=`git status --short | sed 's/?? //g' | grep 'day'`
dayNumber=`echo $day | egrep -oh '[0-9]'`
git add $day
git commit -m "Complete day $dayNumber"
