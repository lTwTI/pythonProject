import time


def loader(info, timer) -> None:
    chars = '|/-\\'
    pointer = 0

    end_time = time.time() + timer

    print(info)

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        current_char = chars[pointer]
        print(f'\rLoading: {current_char} {remaining_time}s left', end='', flush=True)
        pointer = (pointer + 1) % len(chars)
        time.sleep(0.25)

    print('\rThe download process has been successfully completed.')
