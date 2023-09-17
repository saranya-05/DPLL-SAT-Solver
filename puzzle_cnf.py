import os

size = 5
endl = '0'

red = 0
green = 1
white = 2
blue = 3
yellow = 4
color_start, color_end = red, yellow

british = 5
swedish = 6
danish = 7
norwegian = 8
german = 9
nation_start, nation_end = british, german

tea = 10
coffee = 11
water = 12
beer = 13
milk = 14
drink_start, drink_end = tea, milk

prince = 15
blends = 16
pallmall = 17
bluemasters = 18
dunhill = 19
cigar_start, cigar_end = prince, dunhill

dog = 20
cat = 21
bird = 22
horse = 23
fish = 24
pet_start, pet_end = dog, fish

foo = lambda a, b: a + size * b
color = foo
drink = foo
nation = foo
cigar = foo
pet = foo


def generate_house(start_idx, end_idx, get_property):
    house_formulas = []
    for i in range(start_idx, end_idx + 1):
        category_literals = []
        for house_num in range(1, num_houses + 1):
            category_literals.append(str(get_property(house_num, i)))
        category_literals.append(endl)
        house_formulas.append(' '.join(category_literals))

        for house1 in range(1, num_houses + 1):
            for house2 in range(1, house1):
                house_formulas.append('-{} -{} {}'.format(get_property(house2, i), get_property(house1, i), endl))
            for k in range(start_idx, end_idx + 1):
                if k == i:
                    continue
                house_formulas.append('-{} -{} {}'.format(get_property(house1, i), get_property(house1, k), endl))

    return os.linesep.join(house_formulas)

def pair_relationship(category1, property1, category2, property2):
    formula = []
    for i in range(1, size + 1):
        formula.append('-{} {} {}'.format(category1(i, property1), category2(i, property2), endl))
        formula.append('{} -{} {}'.format(category1(i, property1), category2(i, property2), endl))
    return os.linesep.join(formula)

def neighbor(category1, property1, category2, property2):
    formula = [
        '-{} {} {}'.format(category1(1, property1), category2(2, property2), endl),
        '-{} {} {}'.format(category1(size, property1), category2(size - 1, property2), endl)]
    for i in range(2, size):
        formula.append('-{} {} {} {}'.format(category1(i, property1), category2(i - 1, property2), category2(i + 1, property2), endl))
    return os.linesep.join(formula)

def count_cnf(formula_string):
    literals = set()
    lines = formula_string.split(os.linesep)
    for line in lines:
        literals.update([abs(int(x)) for x in line.split() if x.isdigit()])
    return 'p cnf {} {}'.format(len(literals) - 1, len(lines))



def einstein():
    formula = []
    parameters = [
        (color_start, color_end, color),
        (drink_start, drink_end, drink),
        (cigar_start, cigar_end, cigar),
        (pet_start, pet_end, pet),
        (nation_start, nation_end, nation)]
    formula.extend([generate_house(*p) for p in parameters])

    formula.append('{} {}'.format(nation(1, norwegian), endl))
    formula.append('{} {}'.format(color(2, blue), endl))
    formula.append('{} {}'.format(drink(3, milk), endl))
    formula.append(pair_relationship(nation,british,color,red))
    formula.append(pair_relationship(color, green, drink, coffee))
    formula.append(pair_relationship(nation, danish, drink, tea))
    formula.append(pair_relationship(color, yellow, cigar, dunhill))
    formula.append(pair_relationship(nation, swedish, pet, dog))
    formula.append(pair_relationship(nation, german, cigar, prince))
    formula.append(pair_relationship(cigar, pallmall, pet, bird))
    formula.append(pair_relationship(cigar, bluemasters, drink, beer))
    formula.append(neighbor(pet, horse, cigar, dunhill))
    formula.append(neighbor(cigar, blends, pet, cat))
    formula.append(neighbor(cigar, blends, drink, water))
    for w in range(1, size+1):
        for g in range(size, 0, -1):
            if w-1 <= g <= w:
                continue
            formula.append('-{} -{} {}'.format(
                color(w, white), color(g, green), endl
            ))
            
    formula_strings = os.linesep.join(formula)
    formula_cnf = os.linesep.join([count_cnf(formula_strings), formula_strings])
    return formula_cnf


def generate_reference():
    refs = []
    for i in range(1, size+1):
        for c in ['red', 'green', 'white', 'blue', 'yellow']:
            refs.append('{:4.0f}: color({}, {})'.format(color(i, eval(c)), i, c))
        for n in ['british', 'swedish', 'danish', 'norwegian', 'german']:
            refs.append('{:4.0f}: nation({}, {})'.format(nation(i, eval(n)), i, n))
        for d in ['tea', 'coffee', 'water', 'beer', 'milk']:
            refs.append('{:4.0f}: drink({}, {})'.format(drink(i, eval(d)), i, d))
        for c in ['prince', 'blends', 'pallmall', 'bluemasters', 'dunhill']:
            refs.append('{:4.0f}: cigar({}, {})'.format(cigar(i, eval(c)), i, c))
        for p in ['dog', 'cat', 'bird', 'horse', 'fish']:
            refs.append('{:4.0f}: pet({}, {})'.format(pet(i, eval(p)), i, p))
    return os.linesep.join(sorted(refs))


if __name__ == '__main__':
    with open('einstein.cnf', 'w') as f:
        f.write(einstein())
    with open('reference.txt', 'w') as f:
        f.write(generate_reference())