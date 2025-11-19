"""
KVStore file implementation. The problem is to write a KVStore, with data stored on a block device,
where each block of the block device stores 8 characters.

Keys can be stored in memory, values must be written to the block device, values can be of any size.
The block device file is already provided, offering two APIs:
text


number_of_blocks(): int # size of block device
read(block ID): string
write(block ID, string)

"""


class MockBlockDevice:
    def __init__(self, block_size_bytes=8, num_blocks=24):
        self.block_size_bytes = block_size_bytes
        self.num_blocks = num_blocks
        self.blocks = [bytearray(b"X" * self.block_size_bytes) for _ in range(self.num_blocks)]
        self.print_hello()

    def get_total_size_bytes(self):
        return self.block_size_bytes * self.num_blocks

    def get_number_of_blocks(self):
        return self.num_blocks

    def print_hello(self):
        print(f"hello, I am a block device initialized with: {self.get_total_size_bytes()} bytes")

    def read(self, block_index) -> bytearray:
        """Reads a block and returns its content as a bytearray."""
        if not (0 <= block_index < self.num_blocks):
            raise IndexError("Block index out of range")
        return self.blocks[block_index]

    def write(self, block_index, input_data: bytearray):
        """Writes a bytearray to a block, padding or truncating if necessary."""
        if not (0 <= block_index < self.num_blocks):
            raise IndexError("Block index out of range")

        print(f"WRITING TO {block_index=} {input_data=}")
        if len(input_data) > self.block_size_bytes:
            raise Exception("TOO LONG FOR BLOCK")
        else:
            self.blocks[block_index] = bytearray(input_data)

    def print_contents(self):
        for i in range(self.get_number_of_blocks()):
            print(f"BLOCK: {i}:")
            print(f"{self.blocks[i].decode('utf-8')}:")


"""
a:      "apple is| red and| shiny"
block    01234567|01234567|01234567
block_i  0       |1       |2
i_i      0      7|8     15|16    24|25
    our key's pointer to value can be start:end

    block_idx * 8

key a: insert and dict is now: 
{ a: [0,25] }
pointer is now: 25

"""


class BlockStorageDict:
    def __init__(self, block_device):
        self.block_device = block_device
        self.block_i = 0
        self.block_i_max = self.block_device.get_total_size_bytes()
        self.keys = {}

    def set(self, key: str, val: str):
        if len(val) + self.block_i >= self.block_i_max:
            raise Exception("The block device is full, you cannot insert this value")
        if key in self.keys:
            self._delete_key(key)

        start = self.block_i
        end = start + len(val)
        b.keys[key] = [start, end]
        self.write_val(val, self.block_i, self.block_i + len(val))

    def _delete_key(self, key):
        start, end = self.keys[key]
        self.write_val("".join(["D" for _ in range(start, end)]), start, end)
        del self.keys[key]

    def write_val(self, val, start, end):
        byte_per_block = self.block_device.block_size_bytes
        start_block = start % byte_per_block
        end_block = end % byte_per_block

        val_index = 0
        write_index = start
        block_buf_idx = write_index % byte_per_block
        for block_idx in range(start_block, end_block + 1):
            current = bytearray(self.block_device.read(block_idx))
            while write_index < end:
                block_buf_idx = write_index % byte_per_block
                current[block_buf_idx] = ord(val[val_index])

                write_index += 1
                val_index += 1
                if write_index % byte_per_block == 0:
                    # self.block_device.write(block_buf_idx, current)
                    break

            # print(f"writing current: {current} to block_idx: {block_idx}")
            self.block_device.write(block_idx, current)


mock_device = MockBlockDevice(8, 24)
b = BlockStorageDict(mock_device)
b.set("test", "apple is red and shiny")
print(f"{b.keys=}")

mock_device.print_contents()
