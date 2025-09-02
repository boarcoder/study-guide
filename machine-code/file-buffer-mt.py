'''
Buffer to File System

Implement a system where data is first stored in a buffer
Once the buffer is filled or upon request, data is transferred to a file
Handle edge cases like partial buffer fills
Should allow multiple threads to access buffer.

Notes:
- For this question, you need to write a MockFile class yourself so that you can test your implementation.
- file.write can only write a maximum of n bytes to disk at a time
- ensure thread safety
- Similar to the Read4 problem, where data is first read into a buffer before being written to a file.
'''

import threading

class MockFile:
    def __init__(self, max_bytes_write=8):
        self.max_bytes_write = max_bytes_write
        self.tmp = [None] * max_bytes_write
        self.contents = ''
        # 0-1 lock (binary lock)
        self.lock = threading.Lock()
        self._has_context = False

    def write(self, text: str):
        incoming_bytes = len(text) # utf-8
        if incoming_bytes > self.max_bytes_write:
            return Exception(f"Write rejected. Text is above max_bytes_write: {self.max_bytes_write}",)
        self.contents += ''.join(text)
        print(f'contents here: {self.contents}')

    def open(self):
        locked = self.lock.acquire(blocking=True, timeout=1000)

    def close(self):
        self.lock.release()

class FileBuffer:
    def __init__(self, buf_size=20):
        self.buf_size = buf_size
        self.buf = None
        self.wipe_buf()
        self.b = -1
        self.max_file_write = 8
        self.mfile = MockFile(self.max_file_write)
        pass

    def write(self, text: str):
        i = 0
        write_size = 0
        while i < len(text):                
            if self.b == len(self.buf) - 1:
                self.insert_buf()
            if self.b < len(self.buf):
                self.b += 1
                self.buf[self.b] = text[i]
                i += 1
                write_size += 1
        # completely optional to call this. example call to fill in remaining text.
        self.insert_buf()
    
    def insert_buf(self):
        try:
            self.mfile.open()
            j = 0
            write_size = 0
            while j < self.b + 1:
                to = min(j + self.max_file_write, self.b + 1)
                copy = self.buf[j: to]
                self.mfile.write(copy)
                j = to
                print('text to write to file:', copy)
            self.mfile.close()
            if self.b >= len(self.buf) - 1:
                self.wipe_buf()
            
        except Exception as e:
            print("Error in writing to buffer:", e) 
    
    def wipe_buf(self):
        self.buf = [None] * self.buf_size
        self.b = -1

file_buffer = FileBuffer()
file_buffer.write("the quick dog and the lazy cat ran over to the store or something.")