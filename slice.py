#!/bin/python3
import sys 

CHUNK_SIZE = 512   

def main():
    file_path = sys.argv[1]
    start = eval(sys.argv[2])
    end   = eval(sys.argv[3])
    dest_path = sys.argv[4]

    slice_size = end - start + 1
    remaining  = slice_size
    with open(file_path, 'rb') as in_file:
        with open(dest_path, 'wb') as out_file:
            in_file.seek(start)
            while remaining > 0:
                read_size = CHUNK_SIZE if remaining - CHUNK_SIZE >= 0 else remaining
                chunk = in_file.read(read_size)
                out_file.write(chunk)

                remaining -= CHUNK_SIZE

if __name__ == '__main__':
    main()
