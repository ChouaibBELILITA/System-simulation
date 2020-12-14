import simpy
import numpy as np
from interface import *



def generate_interarrival():
	return np.random.exponential(1./5.0)

def generate_service():
	return np.random.exponential(1. / 2.0)


def CafeShop_run(env, servers ):
	i=0
	while True:
		i +=1
		yield env.timeout(generate_interarrival())
		env.process(customer(env,i,servers))




wait_t =[]
temp_file=[]
temp_arrive=[]

def customer(env, customer, servers):
	with servers.request() as request:
		t_arrivaal = env.now
		print  (env.now ,  'customer {} arrives'.format(customer))

		yield request
		print  (env.now ,  'customer {} is being served '.format(customer))
		temp_file.append(env.now-t_arrivaal)
		yield env.timeout(generate_service())
		print  (env.now ,  'customer {} departs'.format(customer))
		t_depart = env.now
		wait_t.append(t_depart - t_arrivaal)
		temp_arrive.append(t_arrivaal)

obs_times =[]
q_length = []

def observe  (env , servers):
	while True :
		obs_times.append(env.now)
		q_length.append(len(servers.queue))
		yield env.timeout(1.0)

np.random.seed(0)


env = simpy.Environment()
servers  =  simpy.Resource(env, capacity=3  )
env.process(CafeShop_run(env,servers))
env.process(observe(env,servers))


env.run(until=20)

def getTempsMoy():
	result = 0
	for w in wait_t:
		result = result + w
	return result / len(wait_t)

import matplotlib.pyplot as plt
index  = 0

for wa in wait_t:
	index = index + 1
	print ("Customer",index, "| Waited ", wa , "min ")

print(len(wait_t))
print("Temps d'attente moyen " , getTempsMoy())
print(obs_times)
print(q_length)

draw(temp_arrive,temp_file,wait_t)




plt.figure()
plt.hist(wait_t)
plt.xlabel("Waiting time (min) ")
plt.ylabel("Num of customers ")
plt.title("Waiting time ")
plt.show()

plt.figure()
plt.hist(temp_file)
plt.xlabel("temp d'attent file (min) ")
plt.ylabel("nombre de clients ")
plt.title("temp d'attente ")
plt.show()



plt.figure()
plt.step(obs_times,q_length)
plt.xlabel("Time (min) ")
plt.ylabel("Queue length ")
plt.title("Queue Length")

plt.show()











