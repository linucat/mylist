import os

working_path = 'C:/Users/LukeT/Desktop/Github-nkdollar/coinmasterspin.link/app'

os.chdir(working_path)

print('\nCurrent working directory ', os.getcwd(), '\n')

try:
    os.system('python main.py')

    os.system('git add .')
    print('\n---->> git add completed \n')

    os.system('git commit -m "newcrawling')
    print('\n---->> git commit completed \n')

    os.system('git push origin main')
    print('\n---->> git push completed \n')

except:
    print("could not execute command")

