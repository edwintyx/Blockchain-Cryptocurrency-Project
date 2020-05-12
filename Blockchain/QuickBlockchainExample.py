def lightning_hash(data):
    return data + '*'

class Block:
    def __init__(self, data, hash, last_hash):
        self.data = data    # What the data is stored
        self.hash = hash    # A unique hash value depending on the input
        self.last_hash = last_hash  # Creates the link between blocks and other blocks

class Blockchain:
    def __init__(self):
        genesis = Block('gen_data','gen_hash', 'gen_last_hash')

        self.chain = [genesis]
    
    def add_block(self, data):
        last_hash = self.chain[-1].hash         # Assigning last_hash with the genesis hash
        hash = lightning_hash(data + last_hash) # Using new_data + last_hash to generate a new hash
        block = Block(data, hash, last_hash)    # Create a new block instance using hash and last_hash

        self.chain.append(block)    # Add new block instance to the list 

foo_blockchain = Blockchain()
foo_blockchain.add_block('one')
foo_blockchain.add_block('two')
foo_blockchain.add_block('three')

for block in foo_blockchain.chain:
    print(block.__dict__)

