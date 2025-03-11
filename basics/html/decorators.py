def announce(f):
    def wrapper():
        print("about to run a func...")
        f()
        print("done withthe function")
    return wrapper
@announce 
def hello():
    print("helllo world")
hello()