wordbank = ["indentation", "spaces",4]

tlgstudents = ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

#This isn't registering in wordbank so I added it manually.
wordbank.append(4)

choice = int(input("Pick a student number! "))

student_name = tlgstudents[choice]

print(student_name,"always uses",wordbank[2], wordbank[1],"to indent.")
