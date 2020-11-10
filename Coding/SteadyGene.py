'''
Created on Dec 30, 2018

@author: siddardha.teegela
'''

'''
find the length of the smallest possible substring that he can replace to make gene a steady gene?
'''
#!/bin/python

# Complete the steadyGene function below.

def balanced(n, dic):
    bal = True
    for k, v in dic.items():
        if v > n:
            bal = False
            break
    return bal
    
def steadyGene(gene):
    alph = dict()
    for char in gene:
        if char in alph:
            alph.update({char:alph[char]+1})
        else:
            alph.update({char:1})
    
    N = len(gene)
    g_n = N/4
    #gene_freq = Counter(gene)

    min_ans = 10**9
    right = left = 0
    itercount = 0
    while right < N and left < N:
        print('Iteration: ',itercount)
        print(alph)
        print('Right',right)
        print('Left',left)
        if not balanced(g_n, alph):
            print('Alph right',gene[right],alph[gene[right]])
            alph[gene[right]] -= 1
            print('Alph right',gene[right],alph[gene[right]])
            right += 1
        else:
            min_ans = min(min_ans, right - left)
            print('Alph left',gene[left],alph[gene[left]])
            alph[gene[left]] += 1
            print('Alph left',gene[left],alph[gene[left]])
            left += 1
        
        itercount +=1
    print(min_ans)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(raw_input())
    #gene = raw_input()
    #Case 1
    n = 8
    gene = "GAAATAAA"
    result = steadyGene(gene)
    #Case 2
    n = 40
    gene = 'TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC'
    #result = steadyGene(gene)
    #fptr.write(str(result) + '\n')
    #fptr.close()