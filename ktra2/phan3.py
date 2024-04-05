district_names = ["HBT","ĐĐ","HM","HĐ","NTL"]
population = [247100,333300,266800,420900,31800]

max_population_index = population.index(max(population))
min_population_index = population.index(min(population))

print("indices of.")
print("-Most populated dist..:", max_population_index)
print("-Least populated dist..:", min_population_index)

print("Names of:")
print("-Most populated dist..:", district_names[max_population_index])
print("-Least populated dist..:", district_names(min_population_index))


areas = [9.224, 43.35, 12.04, 9.96, 10.09]

population_density = [pop / area for pop, area in zip(population, areas)]
print("Population density of:")
for name, density in zip(district_names, population_density):
    print(f"- {name}: {density}")

average_density = sum(population_density) / len(population_density)
print("Average population density:", average_density)
