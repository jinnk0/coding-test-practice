N = int(input())
colors = input()

start = 0
count = 0
if colors[0] != colors[-1]:
    count += 1
while start != -1:
    current_color = colors[start]
    end = colors.rfind(current_color)
    colors = colors[start:end+1] # 색칠
    count += 1
    if current_color == 'R':
        start = colors.find('B')
    else:
        start = colors.find('R')

print(count)