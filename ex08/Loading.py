import time
import shutil
import sys


def format_time(seconds: float) -> str:
    """
    Format the given time in seconds as MM:SS
    """
    m, s = divmod(int(seconds), 60)
    return f"{m:02d}:{s:02d}"


def format_progress_info(progress: int, width: int, iter: int, i: int) -> str:
    """
    Format progress bar
    """
    # calculate percetange processed
    progress_percentage = progress * 100 // width

    # progress bar format
    progress_bar = f"|{'█' * progress:<{width}}|"

    # Combine format
    progress_info = f"{progress_percentage}%{progress_bar} {i}/{iter}"

    return progress_info


def ft_tqdm(lst: range) -> None:
    """
    Simulate a progress bar for iterating through a range.
    """
    total_iterations = len(lst)

    start_time = time.time()

    width = shutil.get_terminal_size().columns - 30
    bar_width = width - 10

    for i, item in enumerate(lst, start=1):
        # calculate the progress
        completion_fraction = int(i / total_iterations * bar_width)

        # time values
        time_elapsed = time.time() - start_time
        speed = i / time_elapsed
        eta = (total_iterations - i) / speed

        # format time values
        elapsed = format_time(time_elapsed)
        eta_format = format_time(eta)

        # format all progress info
        progress_info = format_progress_info(completion_fraction,
                                             bar_width, total_iterations, i)

        # format time info
        time_info = f"[{elapsed}<{eta_format}, {speed:.2f}it/s]"

        # final output
        output = f"\r{progress_info} {time_info}"
        # because print adds new line by default
        sys.stdout.write(output)
        # flush to ensure output is immediately displayed
        sys.stdout.flush()
        yield item

    # new line after completion

    sys.stdout.write('\n')