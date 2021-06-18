#To the folder
cd /home/lkthedev/Mygit/coinmasterwiki.com

#Pull to update
git pull
echo "Pull done..."

#Run main.py from env python path
env/bin/python3 main.py

#Then do git jobs
git add .
echo 'Add done...'

git commit -m new
echo 'Commit done...'

git push

