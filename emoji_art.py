# first code
for i in range (1,11):
    print('\U0001f600'*i)

print('\n')

# second code
times = 1
while times < 11:
    print('\U0001f600'*times)
    times += 1

print('\n')

# third code - ugly solution
for row in range (1,10):
    how_many_emoji = 1
    emoji = '\U0001f600'
    while how_many_emoji < row:
        emoji += '\U0001f600'
        how_many_emoji += 1
    print(emoji)
