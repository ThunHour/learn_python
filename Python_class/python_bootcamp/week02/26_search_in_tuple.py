def search_in_tuple(tupleInput,search):

    if search not in tupleInput:
        return "Element not found in the tuple"
    else:
        return f"Element found at Index: {tupleInput.index(search)}"

search_in_tuple ((20,15,10,30),10)
