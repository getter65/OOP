import time


def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        f = open(file, 'rb')
    except FileNotFoundError as error:
        print(error)
    else:
        content = f.read()
        f.close()
        return content
    finally:
        end_time = time.time()
        total_time = end_time - start_time
        print(f'Time required for video.mp4 = {total_time}')


video_data = read_file_timed('../data/video1102944790.mp4')
video_2_data = read_file_timed('../video.mp4')