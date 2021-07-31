def letters_range(start, stop, step=None):
    if step is None:
        print([chr(ch) for ch in range(ord(start), ord(stop))])
    else:
        print([chr(char) for char in range(ord(start), ord(stop), step)])


letters_range('p', 'g', -2)


