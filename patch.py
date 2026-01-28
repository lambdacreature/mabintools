#!/bin/python3
import sys

CHUNK_SIZE = 512

def main():
    dest_path  = sys.argv[1]
    start = eval(sys.argv[2])
    patch_path = sys.argv[3]
    out_path   = sys.argv[4]

    with open(dest_path, 'rb') as dest:
        with open(patch_path, 'rb') as patch:
            with open(out_path, 'wb') as out_file:
                remaining = start
                while remaining > 0:
                    read_size = CHUNK_SIZE if remaining - CHUNK_SIZE >= 0 else remaining
                    chunk = dest.read(read_size)
                    out_file.write(chunk)

                    remaining -= read_size
    
                patch_size = 0
                while (chunk := patch.read(CHUNK_SIZE)) != b'':
                    out_file.write(chunk)
                    patch_size += len(chunk)

                dest.seek(start + patch_size)
                while (chunk := dest.read(CHUNK_SIZE)) != b'':
                    out_file.write(chunk)


if __name__ == '__main__':
    main()
