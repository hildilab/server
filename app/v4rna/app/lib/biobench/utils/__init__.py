"""
Utility module
"""

import time, random, md5
import simplejson

to_json_string = simplejson.dumps
from_json_string = simplejson.loads


def listify( item ):
    """
    Makes a single item a single item list, or returns a list if passed a
    list. Passing a None returns an empty list.
    
    >>> listify( 'a' )
    ['a']
    """
    if not item:
        return []
    elif isinstance( item, list ):
        return item
    else:
        return [ item ]


def boolean(string):
    """
    interprets a given string as a boolean:
        * False: '0', 'f', 'false', 'no', 'off'
        * True: '1', 't', 'true', 'yes', 'on'
    
    >>> boolean('true')
    True
    >>> boolean('false')
    False
    """
    string = string.lower()
    if string in ['0', 'f', 'false', 'no', 'off']:
        return False
    elif string in ['1', 't', 'true', 'yes', 'on']:
        return True
    else:
        raise ValueError()


def uid():
    """
    Generates a unique ID.
    """
    t = long( time.time() * 1000 )
    r = long( random.random()*100000000000000000L )
    data = str(t)+' '+str(r)
    data = md5.md5(data).hexdigest()
    return data



# http://code.activestate.com/recipes/499335-recursively-update-a-dictionary-without-hitting-py/
def merge_dict(dst, src):
    stack = [(dst, src)]
    while stack:
        current_dst, current_src = stack.pop()
        for key in current_src:
            if key not in current_dst:
                current_dst[key] = current_src[key]
            else:
                if isinstance(current_src[key], dict) and isinstance(current_dst[key], dict) :
                    stack.append((current_dst[key], current_src[key]))
                else:
                    current_dst[key] = current_src[key]
    return dst