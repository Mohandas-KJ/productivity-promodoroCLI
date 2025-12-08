for rem in range(20,-1,-1):
    min,sec = divmod(rem,60)
    print(f'{min:2d}:{sec:2d}')