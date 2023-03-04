def izveidot_koku(n, vecaki):
    koks = [[] for i in range(n)]
    for i in range(n):
        if vecaki[i] == -1:
            sakne = i
        else:
            koks[vecaki[i]].append(i)
    return koks, sakne

def aprekinat_augstums(koks, virsotne):
    if not koks[virsotne]:
        return 1
    else:
        limeni = [aprekinat_augstums(koks, berns) for berns in koks[virsotne]]
        return max(limeni) + 1

n = int(input())
vecaki = list(map(int, input().split()))

koks, sakne = izveidot_koku(n, vecaki)
augstums = aprekinat_augstums(koks, sakne)

print(augstums)