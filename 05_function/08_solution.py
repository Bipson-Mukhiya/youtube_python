
# def print_kwargs(name, power):
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    # print ("Name", name, "power: ", power)


print_kwargs(name = "alice", power = "flying")
print_kwargs(name = "alice")
print_kwargs(name = "alice", power = "flying", enemy = "dr strange")

