python _scripts/generate_recurring_events.py
python _scripts/archive_old_events.py
python _scripts/build_calendars.py

git config --global user.name 'Steven R. Young'
git config --global user.email 'stevenryoung@gmail.com'
git add _posts/*
git add _archive/*
git commit -m "Automated Site Build" || echo "No changes to commit"
git push origin master || echo "No changes to push"