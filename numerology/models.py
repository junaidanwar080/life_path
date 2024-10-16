from django.db import models

class NumerologyData(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    life_path_number = models.CharField(max_length=10, blank=True, null=True)
    destiny =  models.CharField(max_length=10, blank=True, null=True)
    soul_urge_number = models.CharField(max_length=10, blank=True, null=True)  
    personality_number = models.CharField(max_length=10, blank=True, null=True)  # Personality Number field
    website_link = models.URLField(max_length=200, blank=True, null=True)
 
    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if self.birthdate:
            self.life_path_number = self.calculate_life_path_number(self.birthdate)
        
        if self.name:
            self.destiny = self.calculate_destiny_number(self.name)
            self.soul_urge_number = self.calculate_soul_urge(self.name) 
            self.personality_number = self.calculate_personality_number(self.name)  # Call personality number calculation


        super(NumerologyData, self).save(*args, **kwargs)

    def calculate_life_path_number(self, birthdate):
        year, month, day = birthdate.year, birthdate.month, birthdate.day
        total = sum(int(digit) for digit in f"{year}{month:02d}{day:02d}")
        if total > 22 and total not in [11, 22]:
            total = sum(int(digit) for digit in str(total))
        return str(total)
    

    def calculate_destiny_number(self,name):
        name = name.lower().replace(" ", "")
        alphabet_values = {char: index for index, char in enumerate("abcdefghijklmnopqrstuvwxyz", start=1)}
        total = sum(alphabet_values.get(char, 0) for char in name)
        while total > 9:
            total = sum(int(digit) for digit in str(total))
        return total

    def calculate_soul_urge(self, name):
        vowels = {'A': 1, 'E': 5, 'I': 9, 'O': 6, 'U': 3, 'Y': 7}
        name = name.upper()
        total = sum(vowels[char] for char in name if char in vowels)
        
        while total > 9 and total not in [11, 22, 33]:
            total = sum(int(digit) for digit in str(total))
        return str(total)
    

    def calculate_personality_number(self, name):
        consonants = {
            'B': 2, 'C': 3, 'D': 4, 'F': 6, 'G': 7, 'H': 8, 'J': 1, 'K': 2, 'L': 3,
            'M': 4, 'N': 5, 'P': 7, 'Q': 8, 'R': 9, 'S': 1, 'T': 2, 'V': 4, 'W': 5,
            'X': 6, 'Z': 8
        }
        name = name.upper()
        total = sum(consonants[char] for char in name if char in consonants)
        
        # Reduce the total to a single digit or master number (11, 22)
        while total > 9 and total not in [11, 22, 33]:
            total = sum(int(digit) for digit in str(total))
        
        return str(total)