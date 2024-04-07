resauxDeNerons = [[[2, 3], lambda x: x*2], [[2, 4], lambda x: x*2]]

def predict(x, resauxDeNerons):
    for branche in range(len(resauxDeNerons)):
        y = []  # Reset y for each branch
        for neron in range(len(resauxDeNerons[branche]) - 1):  # Exclude the lambda function at the end
            # Apply the operation with the first element of each neuron
            y.append(x * resauxDeNerons[branche][neron][0] + resauxDeNerons[branche][neron][1])
        x = resauxDeNerons[branche][-1](sum(y))  # Apply the lambda function to the sum of y
    return x

