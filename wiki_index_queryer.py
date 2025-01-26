import wikipedia
query = input("Query: > ")
find_results_using_wikipedia = wikipedia.summary(str(query))
print("\n")
print(find_results_using_wikipedia)
