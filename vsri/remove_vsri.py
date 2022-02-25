import glob

bad = "http://vsri.ucdavis.edu"
good = 'vsri_placeholder'

flist = glob.glob('*/*.html',recursive=True)+glob.glob('*.html',recursive=True)

for f in flist:
    with open(f,'r') as fid:
        s = fid.read()

    print(f)
    instances = 0
    while s.find(bad)>-1:
        s = s.replace(bad,good)
        instances+=1
        
    print('\t replaced %d instances'%instances)
    print()
    with open(f,'w') as fid:
        fid.write(s)
