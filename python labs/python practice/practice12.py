# Practice: write a dog class
# props: name, breed, (anything else you want)
# methods: bark (anything else you want)


class Dog():
    """
    Each dog has a name, breed, and a job.
    """
    def __init__(self, name=None, breed=None, job=None):
        self.name = name
        self.breed = breed
        self.job = job

    def bork(self):
        print(f"Bork, my name is {self.name}. They call me a {self.breed} and my job is {self.job} and now a poem - 'Bark.., Bork..., Battlestar Galatica'")


cujo = Dog('Cujo', 'St. Bernard', "Murderer")
xzibit = Dog('Xzibit', 'Dawg', 'Tax Evader')
snoopy = Dog('Snoopy', 'Beagle', 'Woodstock homie')
Scooby = Dog('Scooby Doo', 'Great Dane', '"Solve" Mysteries')
wishbone = Dog('Wishbone', 'Jack Russel', 'Story Teller')

cujo.bork()
xzibit.bork()
snoopy.bork()
Scooby.bork()
wishbone.bork()
