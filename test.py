import sys
from io import StringIO


def handler_name(event, context):
    print(event)
    code = event['code']
    
    glob = {}
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(code, glob)
    sys.stdout = old_stdout
    
    output = redirected_output.getvalue()
    return output