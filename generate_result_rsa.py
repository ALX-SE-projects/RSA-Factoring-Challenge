
import os
for i in os.listdir('tests/rsa'):
    print(i)
    os.system(f'./_rsa ./tests/rsa/{i} > ./results/rsa/{i}')
