# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [ dct[i] for i in keylist]

def list2dict(L, keylist): return { key : l for (l,key) in zip(L,keylist)}

def listrange2dict(L): return {i : L[i] for i in range(0,len(L))}