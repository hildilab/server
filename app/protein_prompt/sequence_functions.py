
def CleanSequence( seq):
    if seq[0] == ">":
        loc = seq.find( '\n' )
        seq = seq[loc+1:]
    seq.replace( '\n', '')
    return seq


def QuickFix( pathy):
    return pathy.strip().replace('/','_').replace( ' ','_' )


#    return pathy.strip().replace( '@', '_').replace('/','_').replace( '.','_').replace( ' ','_' )
def func_name():
    import traceback
    return traceback.extract_stack(None, 2)[0][2]


def Serialize( form):
    return 'sequence=' + form.sequence.data + '&tag=' + form.tag.data + '&email=' + form.email.data + '&db=' + form.db.data 
    

def WriteLines( feil):
    mstr = ""
    styles=["width:20%","width:20%","width:40%;overflow:hidden","width:20%"]
    with open( feil ) as f:
        for l in f:
            c = l.split()
            if len(c) < 4: continue
            mstr += "<tr>\n";
            for t,col in zip( styles,c):
                mstr+= "<td style=\"" + t + "\"> " + col + "</td>\n"
            mstr += "</tr>\n"
    return mstr

