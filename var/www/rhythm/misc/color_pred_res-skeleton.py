
predRes = ###PREDRES###

helixPos = ###HELIXPOS###

colors = { 'h' : 'red',
           'he' : 'orange',
           'm' : 'green',
           'me' : 'limegreen',
           'w' : 'blue',
           'we' : 'lightblue'
           }

cmd.hide('all')
cmd.show('cartoon')
cmd.color('yellow')

for chain, data in helixPos.iteritems():
    for [begin, end] in data:
        for i in range(begin, end):
            if(chain != 'none'):
                cmd.color('white',"res %s and chain %s"%(i,chain))
            else:
                cmd.color('white',"res %s"%(i))

for chain, data in predRes.iteritems():
    for type, residues in data.iteritems():
        for i in residues:
            if (chain != 'none'):
                name = "%s_%s_%s"%(type,chain,i)
                cmd.select(name, "res %s and chain %s"%(i,chain))
            else:
                name = "%s_%s"%(type,i)
                cmd.select(name, "res %s"%(i))

            cmd.color(colors[type], name)
            cmd.show("sticks", name)
