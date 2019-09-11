def countdown(item):
    print(item)
    if item <= 1:
        return
    else:
        countdown(item - 1)


countdown(5)
