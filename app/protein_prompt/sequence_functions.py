
def CleanSequence( seq):
    if seq[0] == ">":
        loc = seq.find( '\n' )
        seq = seq[loc:]
    seq.replace( '\n', '')
    return seq


def FixEmailString( email):
    return email.replace( '@', '_').replace( '.','_')
