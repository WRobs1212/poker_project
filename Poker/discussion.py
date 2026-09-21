lines = []

try:

    print("opening file...")

    file = open(r"fileInput.txt") #why is the code not showing the file contents?

    file.seek(0)

    print("What the current signatures are...")

    lines = file.readlines()

    for line in lines:

        print(line)

    file.close()

    file = open(r"fileInput.txt", "a") #change to text for an error. why is the code not showing the file contents?

    print("please add in your signature")

    signature = input()

    signature = "\n"+signature

    file.write(signature)
finally:

    print("closing file")

print("done. thank you for adding your signature")
