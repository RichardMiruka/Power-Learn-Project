# assigning same value to multiple variables

site1 = site2 = site3 = "Power Learn project"
print(f"{site1} {site2} {site3}")  # Output: Power Learn project Power Learn project Power Learn project

# trying to assign different values to the same variable will raise an error
try:
    site1 = "Power Learn project 2.0"
    print(f"{site1} {site2} {site3}")
except UnboundLocalError as e:
    print(e)

# you can use a loop or list comprehension to create multiple variables with the same value in one line of code
# you can use a loop or list comprehension to create multiple variables with similar names dynamically
sites = ["Power Learn", "Codecademy", "Free Code Camp"] # list of site names
for i, name in enumerate(sites):
    globals()[f"site{i+1}"] = name
    print(f"site{i+1} = {name}")
    
print("\n")

# now we can access each variable individually using its dynamic name
print(f"Site 1 is called '{site1}' and Site 3 is called '{site3}'")  # Output: Site 1 is called 'Power Learn' and Site 3 is called 'Free Code Camp'
for i in range(1, len(sites)+1):
    print(f"Site {i} is called '{globals()[f'site{i}']}'")  # Output: Site 1 is called 'Power Learn', Site 2 is called 'Codecademy', Site 3 is called 'Free Code Camp'
    var_name = f"site{i}"
    print(f"{var_name}: {globals()[var_name]}")  # Output: site1: Power Learn, site2: Codecademy, site3: Free Code Camp
    print(f"{var_name}: {globals()[var_name]}")  # Output: site1: Power Learn, site2: Codecademy, site3: Free Code Camp
    print(f"{var_name}: {globals().get(var_name)}")  # Output: site1: Power Learn, site2: Codecademy, site3: Free Code Camp
    print(f"{var_name}: {globals().get(var_name)}")  # Output: site1: Power Learn, site2: Codecademy, site3: Free Code Camp
    print(f"{var_name}: {globals()[var_name]}")  # Output: site1: Power Learn, site2: Codecademy, site3: Free Code Camp
    print(f"{var_name}: {globals()[var_name]}")  # Output: site1: Power Learn, site2: Codecademy, site3: Free Code Camp