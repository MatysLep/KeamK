from Tirage import Tirage

print("--- Welcome to KEAMK --- \n \n")
tirage = Tirage(input("Name of the tirage : "))
print()
tirage.set_sort_by()
print()
tirage.add_all_participants()
print()
tirage.add_all_teams()
tirage.insert_participants_in_team()
print()
tirage.show_teams()
