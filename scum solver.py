def scum_solver(scum):
    import itertools
    import json
    
    with open("words_dictionary.json") as json_file:
        words_dict = json.load(json_file)
        
        scum1 = scum.split()
        scum_list = list(scum1[0])
        permutations = list(itertools.permutations(scum_list))

        end_list = [''.join(permutation) for permutation in permutations]
        
        end_list_of_words = []
        
        for element in end_list:
            if element in words_dict.keys():
                if element not in end_list_of_words:
                    end_list_of_words.append(element)
        return end_list_of_words



print(scum_solver("incerdible")) #wpisz tutaj jako argument funkcji rozsypane slowo
