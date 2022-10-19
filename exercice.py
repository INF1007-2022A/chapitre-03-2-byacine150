#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return ((voltage**2)/resistance)

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	if(v1[0]* v2[0] + v1[1]* v2[1] == 0):
		return True
	else: 
		return False

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	somme = 0
	for element in values:
		if element > 0:
			somme = somme + element
	return (somme/len(values))

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	if value != 0:
			twenties = int(value/20)
			tens = int((value - (twenties * 20))/10)
			fives = int((value - (twenties * 20)- (tens * 10))/5)
			twos = int((value - (twenties * 20)- (tens * 10) - (fives * 5))/2)
			ones = (value - (twenties * 20)- (tens * 10) - (fives * 5) - (twos*2))

	return (twenties, tens, fives, twos, ones)

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		pass
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		pass
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
