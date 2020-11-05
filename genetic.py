import random
import numpy as np
from Bird import *

# writes values of birds(w1, w2, b1, b2, and fitness) to text file
def writeGen(birds):
	birds.sort()

	with open ('birds.txt','w') as file:
		for bird in birds:
			file.write(str(bird.w1)+'@')
			file.write(str(bird.w2)+'@')
			file.write(str(bird.b1)+'@')
			file.write(str(bird.b2)+'@')
			file.write(str(bird.fitness))
			file.write('#\n')


# there is a small chances that a bird gets mutated
def mutation(newBirds):
	# 2% mutation rate
	mutate_prob = 2

	hiddenLayer1size = 8
	outputLayer = 1
	input = np.array([[0],[0],[0]])

	for bird in newBirds:
		if random.randrange(1, 101, 1) <= mutate_prob:
			bird.w1 = np.random.randn(hiddenLayer1size, len(input)) * 0.01

		if random.randrange(1, 101, 1) <= mutate_prob:
			bird.w2 = np.random.randn(outputLayer, hiddenLayer1size) * 0.01

		if random.randrange(1, 101, 1) <= mutate_prob:
			bird.b1 = np.random.randn(hiddenLayer1size, 1) * 0.01

		if random.randrange(1, 101, 1) <= mutate_prob:
			bird.b2 = np.random.randn(1,1) * 0.01


def crossover(birds, generation):
	birdTopY = 330
	birdLeftX = 250
	velocity = 0

	birds.sort()
	newBirds = []
	nrBirds = 8

	birds = birds[:nrBirds]
	newBirds += birds

	# function that mutates birds
	mutation(newBirds)

	# crossover magic
	for i in range(60):
		indexes = random.sample(range(nrBirds), 2)
		bird1w1 = np.split(birds[indexes[0]].w1,2)[0]
		bird2w1 = np.split(birds[indexes[1]].w1,2)[1]

		indexes = random.sample(range(nrBirds), 2)
		split = random.randint(2,6)
		bird1w2 = birds[indexes[0]].w2[0][:split]
		bird2w2 = birds[indexes[1]].w2[0][split:]


		indexes = random.sample(range(nrBirds), 2)
		bird1b1 = np.split(birds[indexes[0]].b1,2)[0]
		bird2b1 = np.split(birds[indexes[1]].b1,2)[1]

		indexes = random.sample(range(nrBirds), 2)
		randomBird = random.randint(0,1)

		b2 = birds[indexes[randomBird]].b2
		w1 = np.concatenate((bird1w1,bird2w1), axis=0)
		w2 = np.concatenate(([bird1w2],[bird2w2]), axis = 1)
		b1 = np.concatenate((bird1w1,bird2w1), axis=0)
		input = np.array([[0],[0],[0]])

		newBirds.append(Bird(input,w1,w2,b1,b2,birdLeftX,birdTopY,velocity,0))

	return newBirds
