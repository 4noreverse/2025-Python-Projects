camel = input('camelCase:')
listcam = list(camel)
snake = list()
for x in listcam:
    if x.isupper():
        snake.append('_')
    snake.append(x)

snake_case = ''.join(snake).lower()
print(snake_case)
