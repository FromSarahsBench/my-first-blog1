print('Hello, Django girls!')
if 3 > 2:
    print('It works!')
if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not great than 2')
volume = 101
#change volume if too loud or quiet
if volume < 20:
    print("it's kinda quiet.")
elif 20 <= volume < 40:
    print("it's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
def hi():
    print('Hi there!')
    print('How are you?')
def hi(name):
    print('Hi ' + name + '!')
hi("Sarah")
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
for i in range(1, 7):
    print(i)
