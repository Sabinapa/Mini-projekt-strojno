import pandas as pd

df = pd.read_csv('BLACKPixels.csv')

arff_file = 'letters.arff'
with open(arff_file, 'w') as f:
    f.write('@relation output_data\n')
    f.write('\n')

    for i in range(25):
        f.write(f'@attribute letter_{i} numeric\n')

    f.write('@attribute class {A,B,C,C2,D,E,F,G,H,I,J,K,L,M,N,O,P,R,S,S1,T,U,V,Z,Z1}\n')
    f.write('\n')
    f.write('@data\n')

    for index, row in df.iterrows():
        for i in range(25):
            f.write(f'{row.iloc[i]},')
        f.write(f'{row.iloc[25]}\n')

    print('File written successfully!')