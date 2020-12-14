# OOP: objektum orientált programozás
# ez egy elterjedt, népszerű programozási paradigma
# megközelítés, elv: hogyan oldjunk meg programozási problémákat
# más elvi megközelítések is léteznek: funkcionális, procedurális stb.
# coging patterns (ezekből több van)
# nagyon jó és hasznos, de ne legyél túl elvakult vele,
# nem minden esetben a jó megoldás
# 2 célja van: logikai hierarchiába szervezni az objektumokat

# egy lista elemeinél fejben kell tartanom, melyik mit jelent
# összezavarodhatok, hogy pl. melyik a pontszám, az első vagy a második szám
player = ['John', 23, True, 54]

# egy fokkal jobb a helyzet, ha dictionaryt csinálok, mert tudom a propertykről, hogy mit jelentenek
player1 = {'name': 'John', 'age': 23, 'alive': True, 'score': 54}

print(player1['name'])

player2 = {'name': 'John', 'age': 23, 'alive': True, 'score': 54}

# ha objektum orientáltan gondolkodom,
# csinálhatok egy Player osztályt, amit példányosítok

# osztály deklarálása (általában nagy betűvel szoktuk)

# ez egy absztrakt osztály, teszt példa


class Animal:
    alive = True
    # az osztályon belül tudok definiálni különböző függvényeket
    # osztályon belüli függvény:

    # az __init__ metódus class-on belül: konstruktor függvény
    # speciális függvény, minden példányosításnál automatikusan lefut
    def __init__(self, age, max_age):
      # a self speciális kulcsszó, a később létejött objektum példányra utal
      # a self kulcsszó minden metódusnak az első paramétere kell legyen
        self.age = age
        self.max_age = max_age
        print('Animal is initialized')

    # osztályon belüli függvény: metódusnak hívják (method)
    def eat(self):
        print("eating")

    def aging(self):
        self.age = self.age + 1
        if self.age >= self.max_age:
            self.alive = False

    # működést is tudok rendelni az állat osztályhoz
    # ez az állat nem változó még itt
    # úgy tudok változót csinálni, hogy:

    def die(self):
        print('Animal is dead')
        self.alive = False


# osztály példányosítása:
# létrehoz egy változót, aminek a típusa class
# olyan folyamat, amely során létrejön az osztályból egy objektum példány
# példányosításkor az osztály bemeneti paraméterei az __init__ függvény bemeneti paramétere...
my_animal = Animal(10, 50)
my_animal2 = Animal(50, 100)
print(my_animal2.age)
# a my_animal változó típusa: class (objektum példány)
print(type(my_animal))
print(my_animal.age)
my_animal.aging()
print(my_animal.age)
print(my_animal.alive)
my_animal.die()
print(my_animal.alive)
# nem csak kulcsérték párokat, hanem függvényeket is tudnak tárolni

# ez egy üres osztály
# a pass igazából semmit nem csinál


class MyClass:
    pass

# OOP-nek akkor jön elő igazából az eleje, amikor:

# öröklődés: a Dog osztály az Animal osztály minden tulajdonságát örökli
# kivonni nem lehet valamit a már meglévő tulajdonságok közül
# de felülírni, módosítani lehet őket


class Dog(Animal):
    name = ''

    def barking(self):
        print('{} is barking! Vau Vau!'.format(self.name))


class Cat(Animal):
    name = ''

    def meow(self):
        print('{} is meowing! Miau Miau!'.format(self.name))


my_dog = Dog(10, 15)
my_dog.name = 'Bodri'
print(my_dog.alive)
print(my_dog.name)
my_dog.aging()
print(my_dog.age)

# még 1 szinttel lejjebb lévő osztály
# sajátos tulajdonságokkal


class Chiwawa(Dog):
    height = 22
    # 2 aláhúzással kezdődő property vagy metódus nevek private-ek lesznek
    # private property: az objektum példány nem férhet hozzá
    __color = 'white'

    # a Dog osztály metódusát felülírjuk az alosztályban
    def barking(self):
        test = 'valami'
        print('Chiwawa!')

    def get_color(self):
        print(self.__color)


my_chiwawa = Chiwawa(5, 15)
my_chiwawa.barking()
# my_chiwawa.__color # << errort dob!

# csináltunk egy metódust, ami hozzáfér a privát property-hez
my_chiwawa.get_color()

# print(my_chiwawa.test) <<< error

# gorilla banana problem: kérek egy banánt, de nem csak banánt kapok, hanem a gorilla hozza magával az egész dzsungelt :D
# robosztussá válik egy idő után, ha nem elég jól tervezi meg az osztályait az ember

my_chiwawa.height = 100
print(my_chiwawa.height)
