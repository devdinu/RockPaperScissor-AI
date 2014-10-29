import random, operator
import os.path 

file_name = "persist_smilelearner_data"


print "bot played: ", input

# helper : file handler
def persist_data(game_data):
	print "writting to file : ", game_data
	file = open(file_name, "w")
	file.write(str(game_data))
	file.close()

def read_data(): #just reading one line?
	early_data = open(file_name, 'r').read()
	print early_data, "in file."
	return eval(early_data)


gd = {} #game_data

if not os.path.isfile(file_name):
	gd["valid_outputs"]  = ["R", "P", "S"]
	gd["move_count"]  = {'R':0, 'P':0 ,'S':0}
	gd["winner"]  = {"R":"P" , "P":"S", "S":"R"}
	gd["past_moves"] = ""
	gd["move_playe_indexes"] = {'R':[],'P':[],'S':[]}
	gd["count"]=0
	persist_data(gd)
else:
	gd = read_data()

if input:
	gd["move_count"][input]+=1
	gd["past_moves"] += input
	gd["count"] += 1 
	gd["move_playe_indexes"][input] = gd["count"]
	persist_data(gd)

def get_random_output(valid_outputs):
	return  random.choice(valid_outputs)

def random_and_not_same_as_last(valid_outputs):
	return random.choice(rem_elem(valid_outputs, input))

def process():
	if not input:
		return get_random_output(gd["valid_outputs"])
	elif get_winner_tuple_of_most_used_elems(gd["move_count"])[1] < 10:
		return random_and_not_same_as_last(gd["valid_outputs"])
	else:
		return get_winner_tuple_of_most_used_elems(gd["move_count"])[0]

def rem_elem(old_arr, element):
	new_array  = list(old_arr)
	new_array.remove(element)
	return new_array

def get_winner_tuple_of_most_used_elems(dicts):
	return max(dicts.iteritems(), key= operator.itemgetter(1))


def debug_data():
	print gd



debug_data()
output = process()


