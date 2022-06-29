with open("txt.txt", "w") as file:
    file.write("|---|---|\n")
    ur = "https://github.com/1darshanpatil/EulerProject/tree/main/%23"
    for _ in range(1, 14):
        url = f"{ur}{_}problem"
        ind = f"#{_}"
        ele = f"#{_}problem"
        file.write(f"|{ind}|[{ele}]({url})|\n")
        
