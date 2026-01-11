cache = {}
def get_in_cache_else_return(function, function_name, *args,**kwargs):
    cache_key=f"{function_name}-{args}"
    if cache_key in cache:
        print("cache exists")
        return cache[cache_key]
    else:
        cache[cache_key] = function(*args,**kwargs)
        return cache[cache_key]

def a(b:int):
    return b+1

print(get_in_cache_else_return(a,"a",1))
# 2
print(get_in_cache_else_return(a,"a",1))
# Cache exist | 2