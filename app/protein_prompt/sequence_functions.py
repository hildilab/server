
def CleanSequence( seq):
    if seq[0] == ">":
        loc = seq.find( '\n' )
        seq = seq[loc:]
    seq.replace( '\n', '')
    return seq


def FixPath( pathy):
    return pathy.strip().replace( '@', '_').replace('/','_').replace( '.','_').replace( ' ','_' )
