#!/bin/python3
import sys 

CHUNK_SIZE = 512   

def main():
    target_path = sys.argv[1]
    start  = eval(sys.argv[2])
    end    = eval(sys.argv[3])
    out_path =    sys.argv[4]

    slice_size = end - start + 1
    remaining  = slice_size
    with open(target_path, 'rb') as target_file:
        with open(out_path, 'wb') as out_file:
            target_file.seek(start)
            while remaining > 0:
                read_size = CHUNK_SIZE if remaining - CHUNK_SIZE >= 0 else remaining
                chunk = target_file.read(read_size)
                out_file.write(chunk)

                remaining -= CHUNK_SIZE

if __name__ == '__main__':
    main()
