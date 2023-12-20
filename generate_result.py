
import os
for i in os.listdir('tests/factors'):
    print(i)
    os.system(f'./_factors ./tests/factors/{i} > ./results/factors/{i}')
