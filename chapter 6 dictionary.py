eats={"kratika":"burger",
      "kartik":"maggie",
      "tanu":"chilli potato",
      "babblu":"roti"}
print("dictionary eats is= ",eats)
print("Kratika eats ",eats["kratika"])
print("tanu eats ",eats["tanu"])
eats["chhavi"]="rajma"
print("dictionary after adding an key is= ",eats)
del eats["babblu"]
print("dictionary after deleting an key is= ",eats)
new_eats = eats.copy()
print(new_eats)
new_eats.update({"anshu":"chole"})
print("new eats dictionary is= ",new_eats)
print("eats dictionary is= ",eats)

