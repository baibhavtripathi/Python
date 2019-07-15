friends = ['ama','ram','shyam']
timenosee = [1,4,8]

print(
    {
        friends[i]:timenosee[i]
        for i in range(len(friends))
        if timenosee[i]>1
    }
)