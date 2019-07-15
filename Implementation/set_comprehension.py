'''
friends = ['ram','aam','sam','jam']
partyer = ['tity','namu','ram','sam']

party_p = {
    names for names in set(friends).intersection(set(partyer))
}
print(party_p)
'''

friends = {'ram','aam','sam','jam'}
partyer = {'tity','namu','ram','sam'}

party_p = {
    names for names in (friends).intersection((partyer))
    if names != 'ram'
}
print(party_p)