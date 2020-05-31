
def orginiseFaces(faces):
    import itertools
    a = list(itertools.permutations(faces, len(faces)))
    for i in a:
        print("cube({},[{},{},{}],".format(i[0], i[1], i[2], i[3]))

def all_metarules():
    list = [
    'metarule([P,Q], [P,A,B], [[Q,A,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,B,A]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A],[R,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,C],[P,C,B]]).',
    'metarule([P,Q], [P,A],[[Q,A]]).',
    'metarule([P,Q,R], [P,A], [[Q,A],[R,A]]).',
    'metarule([P,Q,B], [P,A,B], [[Q,A],[Q,B]]).',
    'metarule([P,Q,R], [P,A], [[Q,A,B],[R,B]]).',
    'metarule([P,Q,X], [P,A], [[Q,A,X]]).',
    'metarule([P,Q,X], [P,A,B], [[Q,A,B,X]]).',
    'metarule([P,Q,R], [P,A], [[Q,A,B]]).',
    'metarule([P,A], [P,A,_B], []).',
    'metarule([P,B], [P,_A,B], []).',
    'metarule([P,Q,X,Y], [P,X,A], [[Q,Y,A]]).',
    'metarule([P,Q], [P,A], [[Q,A]]).',
    'metarule([P,Q,R], [P,A], [[Q,A],[R,A]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,B]]).',
    'metarule([P,Q,F], [P,A,B], [[Q,A,B,F]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,A]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,B]]).',
    'metarule([P,Q], [P,A], [[Q,A]]).',
    'metarule([P,Q,R], [P,A], [[Q,A],[R,A]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,B]]).',
    'metarule([P,Q,F], [P,A,B], [[Q,A,B,F]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,A]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,B]]).',
    'metarule([P,Q,R], [P,A], [[Q,A,B],[R,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,B,C]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,C], [P,C,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,B]]).',
    'metarule([P,Q,F], [P,A,B], [[Q,A,B,F]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]).',
    'metarule([P,Q,F], [P,A,B], [[Q,A,B,F]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]).',
    'metarule([P,Q], [P,A], [[Q,A]]).',
    'metarule([P,Q,B], [P,A], [[Q,A,B]]).',
    'metarule([P,Q,F], [P,A,B], [[Q,A,B,F]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A],[R,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,C],[P,C,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,B,A]]).',
    'metarule([P,Q], [P,A,B], [[Q,B,C],[P,A,C]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,B,A]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]).',
    'metarule([P,Q],([P,A,B]:-[[Q,A,B]])).',
    'metarule([P,Q,R],([P,A,B]:-[[Q,A,C],[R,C,B]])).',
    'metarule([P,Q,R], [P,A,B], [[Q,B,A],[R,A]]).',
    'metarule([P,Q,R], [P,A], [[Q,A,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A],[R,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,A]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,C],[P,C,B]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A],[R,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,A]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,A,B]]).',
    'metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]).',
    'metarule([P,Q,X], [P,A,B], [[Q,A,B,X]]).',
    'metarule([P,Q], [P,A,B], [[Q,A,C],[P,C,B]]).',
    'metarule([P,Q,X], [P,A], [[Q,A,X]]).',
    'metarule([P,Q,X], [P,A,B], [[Q,A,B,X]]).']

    print(list)

    res = [] 
    for i in list: 
        if i not in res: 
            res.append(i)

    for i in res:
        print(i)

    print(res)

def main():
    orginiseFaces(['p_1','p_2','p_3','p_4'])
    print("hahahahah")

    all_metarules()



if __name__ == "__main__":
    main()


